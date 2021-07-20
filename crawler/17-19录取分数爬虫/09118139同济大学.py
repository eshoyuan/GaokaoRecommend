# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:24:07 2020

@author: Minghao Wang 09118139
"""
import csv
import requests
import bs4
from bs4 import BeautifulSoup
url='http://bkzs.tongji.edu.cn/index.php?classid=3394&action=search'
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
year_list=["2019","2018","2017"]
province_list=["安徽省","北京市","福建省","甘肃省","广东省","广西壮族自治区","贵州省","海南省","河北省","河南省","黑龙江省","湖北省","湖南省","吉林省","江苏省","江西省","辽宁省","内蒙古自治区","宁夏回族自治区","青海省","山东省","山西省","陕西省","上海市","四川省","天津市","西藏自治区","新疆维吾尔自治区","云南省","浙江省","重庆市"]
data_list=[]
for year in year_list:
    for province in province_list:
        data_list.append([year,str(province)])
headers={'User-agent':user_agent, 
         'Cookie':'PHPSESSID=gjq58u2blsee30j1s03e6nkemg; Hm_lvt_b3b075d90cc24dcb1d5795260f02e2d6=1589426342; Hm_lpvt_b3b075d90cc24dcb1d5795260f02e2d6=1589426390'
         }
keys=['year','province']
list1=[]  #list1 is used to store data in each cycle
list_all=[]     #list_all is used to store all data
#for data in data_list:
    #print(dict(zip(keys,data)))
for data in data_list:
    response=requests.post(url,headers=headers,data=dict(zip(keys,data)))
    soup=BeautifulSoup(response.text,'html.parser')
    result=soup.find('table',{'class':"admissions_table"})
    if isinstance(result,bs4.element.Tag):     # important! delete type<nonetype>
        result=result.find_all('tr')
        for item in result:
            tags=item.find_all('td')
            for i in data:
                list1.append(i)   # add year and province to list1
            for tag in tags:
                list1.append(tag.get_text())  # for list1, there is only one piece of info per cycle!
            list_all.append(list1)
            #print(data)
            #print(list1)
            list1=[]
#print(list_all)

###进行到这一步为止，已经将所有数据爬取备份成功，后面进行的是数据处理###

###数据处理部分###
for i in list_all:
    if i in data_list:
        list_all.remove(i)  #移除掉原本的空集(添加data之后变成了和data_list里面元素一样的list)
available_class=['本科一批','第一批本科']
temp_list=[]
for i in list_all:
    if i[2] in available_class:
        temp_list.append(i)
for item in temp_list:
    item.insert(0,"同济大学")
    item.append("09118139王明灏")
#print(temp_list)
result_list=temp_list
for item in result_list:
    item.pop(3)     #pop title"本科一批"
    item.pop(5)     #pop max score, and it is not continuous 
    item.pop(5)     #pop average score
delete_list=["总计","合计","合计（少）","合计（汉）","合计(少)","合计(汉)"]
for item in result_list:
    if item[4] in delete_list:
        result_list.remove(item)
#print(result_list)
with open("D:\seu-2020\SoftwarePractise\TJUscore.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["College","Year","Province","Category","Major","Score","Contributor"])
    writer.writerows(result_list)
#print("done")