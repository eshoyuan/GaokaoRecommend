import urllib3 as u
from bs4 import BeautifulSoup as bs
import csv

http = u.PoolManager()
host_url = r'http://zhsh.cugb.edu.cn/'

# 获得省份列表
province_response = http.request('GET', host_url+'fractionLine.action')
province_soup = bs(province_response.data)
province_select = province_soup.find_all(id='selectedId')
province_options = province_select[0].find_all('option')[1:] # 去除用作标题的第一项
provinces = {} # 省份字典，键=ID, 值=省份，ID在后续构造form表单时使用
for option in province_options:
    provinces[option['value']] = option.contents[0]

# 爬取
data = [] # 存储所有分数线信息的列表
for year in ['2019', '2018', '2017', '2016']: # 年份从2016-2019
    for value, province in provinces.items():
        form = {'province': province,
                'cmsFractionLine.cmsCity.code': value,
                'cmsFractionLine.year': year} # 构建form表单
        response = http.request('POST', host_url+'doSearchFractionLine.action', fields=form) # 此处返回一个html
        soup = bs(response.data)
        table = soup.find_all('table')[0].tbody # 从html里找到分数线table
        if table.contents:
            item_list = table.find_all('tr') # 每行tr为一个专业，放入list中
            for item in item_list:
                column_list = item.find_all('td')
                category = column_list[2].contents[0] # 每个专业tr中第3个td为科类
                major = column_list[3].contents[0] # 第4个td为专业名
                min_score = column_list[-2].contents[0] # 倒数第2个td为最低分
                data.append(['中国地质大学（北京）', year, province, category, major, min_score, '09118120徐浩卿'])

# 写入CSV
with open('09118120徐浩卿-中国地质大学（北京）.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])
    writer.writerows(data)
