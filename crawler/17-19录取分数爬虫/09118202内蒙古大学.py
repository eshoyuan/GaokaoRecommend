import requests
import jieba
import pandas as pd
from bs4 import BeautifulSoup

df_total = pd.DataFrame(columns=['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])
list_data = []  # 用于存储数据


def get_data(location, c, y, p, ca):

    s_url = location  # 分数线页面地址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    params = {"show_ram": 1}

    s_response = requests.get(s_url, headers=headers, params=params, verify=False)  # Get方式获取网页数据
    s_response.encoding = 'utf-8'

    s_soup = BeautifulSoup(s_response.text, 'html.parser')

    data = s_soup.select('#vsb_content')  # 选出数据表格部分

    # 爬取表格中的数据
    trs = data[0].find_all('tr')
    # 传入的数据初始化
    s_college = c
    s_year = y
    s_province = p
    s_category = ca
    major = ''
    min_score = ''
    contributor = '09118202赵基藤'

    # 读取每行数据
    for tr in trs[0:]:
        td = tr.find_all('td')
        col_len = len(td)

        # 读取表格标题
        if col_len == 1:
            s_title = td[0].get_text().strip()
            seg = jieba.lcut(s_title)  # 分词
            s_college = seg[0]
            s_year = seg[1]
            s_province = seg[3]

            # 找到文理科，若没有则写为无
            for string in seg[4:]:
                if ('文' in s_category) or ('理' in s_category):
                    break
                elif ('文' in string) or ('理' in string):
                    s_category = string
                else:
                    s_category = '无'

        # 获得专业和分数线
        if col_len >= 7:
            major = td[2].get_text().strip()
            min_score = td[5].get_text().strip()

        # 打印和存储数据
        s_list = [s_college, s_year, s_province, s_category, major, min_score, contributor]
        if ('' not in s_list) and ('总计' not in s_list) and (s_list not in list_data):
            print(s_list)
            list_data.append(s_list)
            df_total.loc[len(df_total)] = s_list


# 主代码部分，爬取八个页面
for i in range(1, 8):
    url = 'https://zhaosheng.imu.edu.cn/copy_1_list.jsp?a4t=8&a4p='+str(i)+'&a4c=15&urltype=tree.TreeTempUrl&wbtreeid=1099'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    params = {"show_ram": 1}

    response = requests.get(url, headers=headers, params=params, verify=False)  # Get方式获取网页数据
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('a')  # 获得网页地址

    for links in tags:
        link = links.get('href')
        title = links.get('title')  # 获得网页标题

        # 筛选出符合要求的页面
        if (title is not None) and ('分数线' in title) and ('本科一批' in title):
            title = title.replace('\u200b', '')
            words = jieba.lcut(title)  # 分词
            college = words[0]
            year = words[1]
            province = words[3]
            category = words[-4]

            # 爬取下一级页面
            sub_url = 'https://zhaosheng.imu.edu.cn/' + link
            get_data(sub_url, college, year, province, category)


print(df_total)
# 保存为csv文件
df_total.to_csv('E:/untitled/score_data_09118202赵基藤.csv', sep=',', header=True, index=True, encoding='utf_8_sig')












