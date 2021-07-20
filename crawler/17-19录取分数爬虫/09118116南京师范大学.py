import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# 创建dataframe
columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor']
df = pd.DataFrame(columns=columns)
college = '南京师范大学'
contributor = '09118116李春澍'
year_list = [2017, 2018, 2019]  # 年份
max_page = [44, 37, 38]  # 最大页数

# UA模拟
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/54.0.2840.99 Safari/537.36'}

for year, mpage in zip(year_list, max_page):
    for page in range(1, mpage):
        url = 'http://bkzs.njnu.edu.cn/fsx/index?NF={}&SF=&page={}'.format(year, page)  # 网页链接
        html = requests.get(url, headers=headers)  # 使用get获取静态信息
        soup = BeautifulSoup(html.text, 'lxml')  # 使用BeautifulSoup解析html

        for tr in soup.find_all('tr', class_='tb_info_all_content'):  # 发现所有的信息行的类都是tb_info_all_content
            tds = tr.find_all('td')

            row = [college, tds[0].text, tds[1].text, tds[3].text, tds[2].text, tds[6].text, contributor]
            row = pd.Series(row, index=columns)
            df = df.append(row, ignore_index=True)  # 数据帧插入一行

        time.sleep(1)  # 防止被屏蔽

df.to_csv('09118116李春澍-南京师范大学.csv', index=False, encoding='gbk')