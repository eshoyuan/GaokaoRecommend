# -*- coding: utf-8 -*-
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_webcontent(year):
    url = 'https://www.gotopku.cn/programa/admitline/7/' + year + '.html'
    # 因为是静态，所以用get获取
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data_list = []

    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            # 这里只考虑一批，不考虑提前批次，港澳台侨联招无批次概念
            if tds[0].contents[0] == '港澳台侨联招' or tds[1].contents[0] == '一批':
                # 文科数据
                data_list.append({
                    'College': '北京大学',
                    'Year': year,
                    'Province': tds[0].contents[0],
                    'Category': '文科',
                    'Major': 'all',
                    'Score': tds[2].contents[0],
                    'Contributor': '09118102张妍',
                })
                # 理科数据
                data_list.append({
                    'College': '北京大学',
                    'Year': year,
                    'Province': tds[0].contents[0],
                    'Category': '理科',
                    'Major': 'all',
                    'Score': tds[3].contents[0],
                    'Contributor': '09118102张妍',
                })
            # 上海、浙江单独考虑，因为他们不分文理
            if tds[0].contents[0] == '上海' or tds[0].contents[0] == '浙江':
                # 上海只有'限物理科目'和'不限科目'，不过每年的说法不太一样，所以这里两个if统一一下
                if '物理科目' in tds[1].contents[0]:
                    tds[1].contents[0] = '物理科目组'
                if '不限科目' in tds[1].contents[0]:
                    tds[1].contents[0] = 'all'
                data_list.append({
                    'College': '北京大学',
                    'Year': year,
                    'Province': tds[0].contents[0],
                    'Category': '-',
                    'Major': tds[1].contents[0],
                    'Score': tds[4].contents[0],
                    'Contributor': '09118102张妍',
                })
    return data_list


def save_csv(data_list):
    df = pd.DataFrame(data_list)
    path = '北京大学updated.csv'
    # 判断文件是否已经存在，如果不存在，就创建；存在，就追加
    if os.path.exists(path):
        df.to_csv(path, index=False, mode='a', header=None, encoding="utf_8_sig")
    else:
        df.to_csv(path, index=False, encoding="utf_8_sig")

if __name__=='__main__':
    save_csv(get_webcontent('2020'))
    save_csv(get_webcontent('2019'))
    save_csv(get_webcontent('2018'))
    save_csv(get_webcontent('2017'))
