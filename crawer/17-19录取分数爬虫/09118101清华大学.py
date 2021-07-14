# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:55:28 2020

@author: Sylvia G
"""

import requests
import re
import csv
import pyquery
from bs4 import BeautifulSoup

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
city = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州',
        '云南', '陕西', '甘肃', '青海', '北京', '天津', '上海', '重庆', '西藏', '内蒙古', '广西', '宁夏', '新疆', '港澳台联招']

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
headers = {'User-Agent': user_agent}
# 网址
url1 = 'http://www.join-tsinghua.edu.cn/publish/bzw2019/12182/2019/20190711140133204531696/20190711140133204531696_.html'
url2 = 'http://www.join-tsinghua.edu.cn/publish/bzw2019/12182/2019/20190515235707374827514/20190515235707374827514_.html'
url3 = 'http://www.join-tsinghua.edu.cn/publish/bzw2019/12182/2019/20190516001226652554876/20190516001226652554876_.html'


def get_text(url):  # 获取网页源码文本
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("无法连接")


def pre_process(url):  # 对源码进行处理，分割文本，使之变成列表形式
    data = get_text(url)
    d = pyquery.PyQuery(data)
    texts = d('p').text()  # 以<p>标签为节点，取其中文本
    thelist = texts.split()  # 以空格为分隔符，分割文本
    return thelist


# url = "http://www.join-tsinghua.edu.cn/publish/bzw2019/12182/index.html"
# r=get_text(url)
# soup=BeautifulSoup(r,"html.parser")
# for a in soup.find_all('a'):
#    print(a.get('href'))

list1 = pre_process(url1)
list2 = pre_process(url2)
list3 = pre_process(url3)

total_list = []  # 所有网页经处理过的文本列表合为一个总列表，含三个列表元素
total_list.append(list1)
total_list.append(list2)
total_list.append(list3)


# print(total_list)


def get_data(datalist, category, score, stop=False):  # 对每一条数据进行处理，提取出专业及录取分数信息
    lenth = len(datalist)
    # 如果循环遇到数字，则表明数字前的非数字字符为专业信息，以布尔值stop的变化来区分
    for i in range(lenth):
        if stop == False:
            for a in datalist[0]:

                if a not in number:
                    if stop == True:
                        break
                    category += a

                if a in number:
                    score += a
                    stop = True
            datalist.pop(0)

        if stop == True:
            return [category, score]


# 创建并写入csv文件
csvFile = open("C:/Users/Sylvia G/Desktop/09118101高捷-清华大学.csv", "w+", newline='')
try:
    year = ''
    writer = csv.writer(csvFile)
    writer.writerow(('College', 'Year', 'Province', 'Category', 'Score', 'Contributor'))  # 表头部分
    for l in total_list:

        for i, data in enumerate(l):

            province = ''
            category = ''
            score = ''

            pattern = r'：|；|，|-'  # 以标点分割文本，形成以每一省份数据为元素的列表
            data = re.split(pattern, data)

            # print(data)
            if i == 0:
                year = data[0]

            if i != 0:
                if data[0] in city:  # 以省份名开头的list才是需要的数据
                    province = data[0]
                    data.pop(0)  # 获取省份信息后将其pop掉

                    lenth = len(data)
                    for a in range(lenth):
                        if len(data) != 0 and data[0] != '':
                            # print(data)
                            c_s_list = get_data(data, category, score)
                            category = c_s_list[0]
                            score = c_s_list[1]
                            # print(c_s_list[0],c_s_list[1])
                            # print(c_s_list)

                            # print(year,province,category,score)
                            writer.writerow(['清华大学', year, province, category, score, '09118101高捷'])  # 写入一行数据
                            category = ''
                            score = ''
                        if len(data) == 0:
                            break

finally:
    csvFile.close()
