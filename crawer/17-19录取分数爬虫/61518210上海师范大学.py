# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:49:01 2020

@author: Lenovo
"""
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

#获取网页中的文本信息
def parse_page(url):
    response = requests.get(url)
    response.encoding="utf-8"
    soup = BeautifulSoup(response.text,"html.parser")
    return_list=soup.find_all('td')
    target_list=[]
    for info in return_list:
        target_list.append(info.get_text())
    return target_list


#从文本信息中抽取有效信息
def get_Point(target_list):
    number_index=[]#各省存储在target_list中的下标
    Province=[]#存储各省名称
    Art_Point=[]#存储各省文科分数线
    Science_Point=[]#存储各省理科分数线
    
    #获得各省名称和其存储在target_list中的下标，以用来提取各省的文理科分数线
    for i in range(0,len(target_list)):
        target_list[i]=target_list[i].strip()#先除去字符串内的空格
        if target_list[i].isdigit():
            a=int(target_list[i])
            if a<100:
                number_index.append(i)
                Province.append(target_list[i+1])

    #先求出整体分数情况
    Point=list(np.zeros(len(number_index)))
    for i in range(0,len(number_index)-1):
        Difference=number_index[i+1]-number_index[i]
        temp_list=[]
        for j in range(1,Difference):
            if target_list[number_index[i]+j].isdigit():
                a=int(target_list[number_index[i]+j])
                temp_list.append(a)
            if target_list[number_index[i]+j][-2:-4:-1]=='外中':
                Length=len(target_list[number_index[i]+j])
                new_list=target_list[number_index[i]+j][0:6:1]
                a=float(new_list)
                a=int(a)
                a1=int(a/1000)
                temp_list.append(a1)
        Point[i]=temp_list
    Point[-1]=[]
    
    #再求出文理科分数线
    for i in range(0,len(Province)):
        Length=len(Point[i])
        if Length>=2:
            Science_Point.append(Point[i][Length-1])
            Art_Point.append(Point[i][Length-2])
        else:
            Science_Point.append("NULL")
            Art_Point.append("NULL")
    return Province,Art_Point,Science_Point

#将读取到的信息写入csv文件
def get_data(Province,Art_Point,Science_Point,year):
    Data=[]
    for i in range(0,len(Province)):
        templist1=[]
        templist2=[]
        if Art_Point[i]!='NULL':
            templist1=['上海师范大学',year,Province[i],'文科','All',Art_Point[i],'61518210吉中旭']
            Data.append(templist1)
        
        if Science_Point[i]!='NULL':
            templist2=['上海师范大学',year,Province[i],'理科','All',Science_Point[i],'61518210吉中旭']
            Data.append(templist2)
    return Data

#读取2019年录取分数线网页信息，并解析获得录取分数文本信息
url_2019='http://ssdzsb.shnu.edu.cn/ea/20/c26799a715296/page.htm'
target_list_2019=parse_page(url_2019)

#提取各省分数线
Province_2019=[]#存储各省名称
Art_Point_2019=[]#存储各省文科分数线
Science_Point_2019=[]#存储各省理科分数线
Province_2019,Art_Point_2019,Science_Point_2019=get_Point(target_list_2019)

#获得数据
Data_2019=get_data(Province_2019,Art_Point_2019,Science_Point_2019,'2019')

#读取2017年录取分数线网页信息，并解析获得录取分数文本信息
url_2017='http://ssdzsb.shnu.edu.cn/ee/b9/c26799a716473/page.htm'
target_list_2017=parse_page(url_2017)

#提取各省分数线  
Province_2017=[]#存储各省名称
Art_Point_2017=[]#存储各省文科分数线
Science_Point_2017=[]#存储各省理科分数线
Province_2017,Art_Point_2017,Science_Point_2017=get_Point(target_list_2017)

#获得数据
Data_2017=get_data(Province_2017,Art_Point_2017,Science_Point_2017,'2017')

#写入csv
tag=['College','Year','Province','Category','Major','Score','Contributor']
Data=Data_2019+Data_2017
biaoge=pd.DataFrame(columns=tag,data=Data)
biaoge.to_csv("61518210吉中旭-上海师范大学.csv")

