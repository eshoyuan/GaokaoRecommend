# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:11:41 2020

@author: 09118133罗琦晴
负责高校：复旦大学——因网页数据格式原因，与老师协调，只用爬取2019年的录取成绩
"""

import requests
from bs4 import BeautifulSoup
import re
import csv


# 爬取网页url，并提取全部表格的信息tables
def get_table(url):
    try:
        # 读取网页并转换
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="lxml")
        # 提取4张表的内容并返回
        tables = soup.find_all(name='tbody')
        return tables
    except:  
        print('无法爬取网页！！！')
    
 
# 第一种表格处理：复旦大学以及复旦大学医学部的大部分省份信息
# table为待处理的表，college为该表的学校名称，category为每个省份的[类型]分类列表
def get_contents_1(table,college,category):
    
    # 建立数据列表，用于储存获取信息
    table_content = []
    
    # 提取行，一行表示一个学校
    row = table.find_all('tr')
    for i in range(len(row)):
        # 跳过表头
        if i == 0 or i == 1:
            continue
        # 提取每行的单元格
        cal = row[i].find_all('td')
        province = cal[0].find('span')# 省份信息
        # 成绩信息：依据类型列表，提取“第一批”成绩对应的单元格
        for j,c in enumerate(category):
            score = cal[4*(j+1)].find('span')
            # 跳过无用信息
            if score.contents[0]=='—':
                continue
            # 记录完整信息
            data = [college,Year,province.contents[0],c,Major,score.contents[0],Contributor]
            table_content.append(data)

    return table_content


# 第二种表格处理：特殊处理复旦大学有关“上海”和“浙江”的信息
# table为待处理的表，college为该表的学校名称，category为每个省份的类型分类
def get_contents_2(table,college,category):
    
    # 建立数据列表，用于储存获取信息
    table_content = []
    
    # 提取所有单元格，再用正则表达式提取所需信息
    td = table.find_all('td')
    # 省份
    province_1 = re.split(r'(\S+)', td[0].text)[1]# 上海
    province_2 = re.split(r'(\S+)', td[5].text)[1]# 浙江
    province = [province_1,province_1,province_2,province_2,province_2,province_2]
    # 专业
    text_1 = re.split(r'(\w+)', td[4].text)
    text_2 = re.split(r'(\w+)', td[-1].text)
    major = [text_1[1],text_1[7],re.sub("[\d]","",text_2[1]),re.sub("[\d]","",text_2[3]), \
             re.sub("[\d]", "", text_2[5]),re.sub("[\d]","",text_2[7])]
    # 成绩
    score = [text_1[5],text_1[-2],re.sub("[\D]","",text_2[1]),re.sub("[\D]","",text_2[3]), \
             re.sub("[\D]","",text_2[5]),re.sub("[\D]","",text_2[7])]
    
    # 记录完整信息
    for i in range(6):
        data = [college,Year,province[i],category,major[i],score[i],Contributor]
        table_content.append(data)
         
    return table_content


# 第三种表格处理：特殊处理复旦大学医学部有关上海和浙江的信息
# table为待处理的表，college为该表的学校名称，category为每个省份的类型分类
def get_contents_3(table,college,category):
    
    # 建立数据列表，用于储存获取信息
    table_content = []
    
    # 提取所有单元格，再用正则表达式处理所需信息
    td = table.find_all('td')
    # 省份
    province_1 = re.split(r'(\S+)',td[0].text)[1]# 上海
    province_2 = re.split(r'(\S+)',td[5].text)[1]# 浙江
    province = [province_1,province_2]
    # 成绩
    score_1 = re.split(r'(\S+)',td[4].text)[1]
    score_2 = re.split(r'(\S+)',td[-1].text)[1]
    score = [score_1,score_2]
    
    # 记录完整信息
    for i in range(2):
         data = [college,Year,province[i],category,Major,score[i],Contributor]
         table_content.append(data)    

    return table_content


# 将数据data表存在名为file_name的CSV文件中
def save_contents(datas,file_name):
    with open(file_name,'w',newline='')as f:
        writer = csv.writer(f)
        writer.writerows(datas)


# 复旦大学招生网2019年录取信息的网址
url = r'http://www.ao.fudan.edu.cn/index!list.html?sideNav=582&ccid=10292&topNav=282&t=1589155849829'
# 调用函数，爬取录取信息的表格
tables = get_table(url)


# 基本信息
Headers = ['College','Year','Province','Category','Major','Score','Contributor']# 表头：学校，年份，省份，类型，专业，录取分数，提供者
College = ['复旦大学','复旦大学医学部']# 学校名称
Year = '2019'# 年份
Category = ['文科','理科','all']# 类型
Major = 'all'# 专业
Contributor = '09118133罗琦晴'


# 根据每张表的特点，调用不同的函数，提取所有有用数据
contents_0 = get_contents_1(tables[0],College[0],[Category[0],Category[1]])# 表格0：复旦大学各省份文理科成绩
contents_1 = get_contents_2(tables[1],College[0],Category[2])# 表格1：复旦大学上海和浙江成绩
contents_2 = get_contents_1(tables[2],College[1],[Category[1]])# 表格2：复旦大学医学部各省份理科成绩
contents_3 = get_contents_3(tables[3],College[1],Category[2])# 表格3：复旦大学医学部上海和浙江成绩


# 将表头和4张表的全部信息整合在一起
all_contents = []
all_contents.append(Headers)
all_contents.extend(contents_0)
all_contents.extend(contents_1)
all_contents.extend(contents_2)
all_contents.extend(contents_3)


# 调用函数，将数据保存在CSV文件中
file_name = r'09118133罗琦晴-复旦大学.csv' #文件名
save_contents(all_contents,file_name)

