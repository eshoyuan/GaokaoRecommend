import requests
from bs4 import BeautifulSoup
import csv
import re

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}


url = 'http://rdzs.ruc.edu.cn/cms/'  # 人大招生网首页
jichu = 'http://rdzs.ruc.edu.cn'  # 每个所需要的网页的基础头

req = requests.get(url, headers=headers)
html = req.text
bf = BeautifulSoup(html, 'lxml')
years = bf.find_all('div', class_='year')


# years1中存储需要的年份名称
# urls中存储每一年下的url
years1 = []
urls = []
for div in years:
    for i, year in enumerate(div):
        if year != '\n':
            years1.append(year.string)
            urls.append(jichu+year.get('href'))
            if i == 5:
                break

pattern1 = re.compile(u"[\u4e00-\u9fa5]+")  # 匹配中文
pattern2 = re.compile(u"\"\S+\"")  # 匹配网址

# 为csv文件写标题
with open("爬取结果.csv",'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])
    
# 每一年循环
for i in range(3):  
    year = years1[i]  # 当前年名称
    year_url = urls[i]  # 当前年的url
    provinces = []  # 当前年有录取记录的省份名称集合
    all_province_urls = []  # 当前年有录取的省份分数线url集合
    
    # 找到地区集合（如网站分的华北地区、东北地区等）
    req = requests.get(year_url, headers=headers)
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    regions = bf.find_all('div', class_='content-place row')
    
    # 对于每一个地区（含多个省份）
    for region in regions:
        region = str(region)
        province_names = pattern1.findall(region)  # 正则化匹配到省份名称集合
        province_urls = pattern2.findall(region)  # 正则化匹配到省份url集合
        provinces.extend(province_names)  # 加入到当前年有录取记录的省份名称集合中
        all_province_urls.extend(province_urls)  # 加入到当前年有录取记录的省份分数线url集合中
        
    # 对于每个省份（去除没有分数线信息的港澳台地区和全国地区）
    for j, province_url in enumerate(all_province_urls[:-4]):
        province = provinces[j]  # 当前省份名称
        url = jichu + province_url[1:-1]  # 当前年、当前省份url
        
        req = requests.get(url, headers=headers)
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        trs = bf.find_all('tr')
        ulist = []
        
        for tr in trs:
            ui = []
            for td in tr:
                ui.append(td.string)
            ulist.append(ui)
        with open("爬取结果.csv",'a', newline='') as f:
            writer = csv.writer(f)
            if j != 8 and j != 10:  # 普通省份信息（分文理科）
                for k in range(1, len(ulist)):
                    writer.writerow(['中国人民大学', year, province, '理科', ulist[k][1], ulist[k][9], '09118103王倩'])
                    writer.writerow(['中国人民大学', year, province, '文科', ulist[k][1], ulist[k][5], '09118103王倩'])
            else:  # 浙江和上海信息（不分文理科）
                for k in range(1, len(ulist)):
                    writer.writerow(['中国人民大学', year, province, '', ulist[k][1], ulist[k][5], '09118103王倩'])
    



