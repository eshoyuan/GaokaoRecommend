
#四川大学的招生信息由链接跳转的方式以表格呈现，需要获取超链接嵌套读取有效信息

from bs4 import BeautifulSoup as bs
import csv
import requests
import pandas as pd
import urllib.parse as up

def category_decision(category_list,title_str):    #通过title属性确定category

    category='null'

    for i in range(len(category_list)):

        if category_list[i] in title_str:

            category = category_list[i]

    if '理' in category and '文理' not in category:

        category='理科'

    elif '文' in category and '文理' not in category:

        category = '文科'

    else:

        category='all'

    return category

def year_decision(year_list, title_str):      #通过title属性确定year

    year = 'null'

    for i in range(len(year_list)):

        if year_list[i] in title_str:

            year = year_list[i]

    return year

def get_url_list(url,header,cate_decision_list,year_decision_list):    #

    resq = requests.get(url, headers=header)

    resq.raise_for_status()

    resq.encoding = resq.apparent_encoding

    html_data = resq.text

    soup = bs(html_data, 'html.parser')  # <class 'bs4.BeautifulSoup'>

    data_tables = soup.find_all('tr')  # 通过soup对解析后的网页进行特定标签的读取，读取所有tr(<class 'bs4.element.ResultSet'>外套列表)

    title_str=soup.find('title').string   #找到title

    category=category_decision(cate_decision_list, title_str)  #由title确定类别

    year=year_decision(year_decision_list, title_str)   #由title确定年份

    province = []

    href = []

    for th in data_tables:

        a_data = th.find_all('a')  # 找到所有有效信息 <class 'bs4.element.ResultSet'>

        for item in a_data:

            href.append(up.urljoin(url,item['href']))    # 读取链接地址

            province.append(item.string)    # 读取省份

    return href,province,[year,category]

def get_all_info(href,label,basic_info,college,contributor):     #得到含有完整信息（可直接写入）的列表

    if len(href)!=len(label):

        return 'data does not match'

    else:

        info=[]

        for i in range(len(label)):

            all_data_table = pd.read_html(href[i])

            data_table=all_data_table[0].loc[1:, 0:2:2]    #只取想要的部分：最低分、专业

            for j in range(1,data_table.shape[0]+1):

                info.append([college,basic_info[0],label[i],basic_info[1],data_table.loc[j][0], data_table.loc[j][2],contributor])    #整合为完整信息

        return info    #输出完整信息列表

def write_info(info, path=''):

    f = open(path + '61518218沈书杨-四川大学.csv', 'w', newline='', encoding='ANSI')

    csv_writer = csv.writer(f)

    csv_writer.writerow(["College", "Year", "Province", "Category", "Major", "Score", "Contributor"])

    for i in range(len(info)):

        csv_writer.writerow(info[i])

    return 0

if __name__ == '__main__':

    category_decision_list = ['不分文理', '理工', '文史']  # 类别

    year_decision_list = ['2019', '2018', '2017']  # 年份

    url_list = ['http://zs.scu.edu.cn/info/1037/2083.htm', 'http://zs.scu.edu.cn/info/1037/2129.htm',
                'http://zs.scu.edu.cn/info/1037/2128.htm',
                'http://zs.scu.edu.cn/info/1037/1493.htm', 'http://zs.scu.edu.cn/info/1037/1489.htm',
                'http://zs.scu.edu.cn/info/1037/1370.htm',
                ]  # 需要爬取的网页

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    college = '四川大学'

    contributor = '61518218沈书杨'

    advanced_info = []

    for url in url_list:
        
        href, label, basic_info = get_url_list(url, header, category_decision_list, year_decision_list)

        advanced_info = advanced_info + get_all_info(href, label, basic_info, college, contributor)

    write_info(advanced_info)
