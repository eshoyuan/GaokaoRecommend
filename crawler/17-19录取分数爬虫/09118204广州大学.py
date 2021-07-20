# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:25:19 2020

@author: 09118204钟倩如
"""

import requests
from bs4 import BeautifulSoup
import csv
headers1={'User-agent':'Mozilla/5.0'}
url1='http://zsjy.gzhu.edu.cn/info/1023/3212.htm'
r1=requests.get(url1,headers=headers1)
r1.encoding='utf-8'
soup1=BeautifulSoup(r1.text,'html.parser')

list1=soup1.find_all('td')
list2=[]
for i in list1:
    list2.append(i.get_text())
#print(list2)

path='09118204钟倩如 - 广州大学.csv'
with open(path,'w',newline='') as f:
    csv_write=csv.writer(f)
    csv_head=['College','Year','Province','Category','Major','Score','Contributor']
    csv_write.writerow(csv_head)

contributor='09118204钟倩如'
college='广州大学'
year=[2019,2018,2017]
province='广东省'

i=6
while i < len(list2):
    with open(path,'a+',newline='') as f:
        csv_write=csv.writer(f)
        data_row=[college,year[0],list2[i],list2[i+1],list2[i+2],list2[i+3],contributor]
        csv_write.writerow(data_row)
    i=i+6

url2='http://zsjy.gzhu.edu.cn/info/1023/3211.htm'
r2=requests.get(url2,headers=headers1)
r2.encoding='utf-8'
soup2=BeautifulSoup(r2.text,'html.parser')

list1=soup2.find_all('td')
list2=[]
for i in list1:
    list2.append(i.get_text())

i=6
while i < len(list2):
    with open(path,'a+',newline='') as f:
        csv_write=csv.writer(f)
        data_row=[college,year[0],list2[i],list2[i+1],list2[i+2],list2[i+3],contributor]
        csv_write.writerow(data_row)
    i=i+6
    
url3='http://zsjy.gzhu.edu.cn/info/1023/2055.htm'
r3=requests.get(url3,headers=headers1)
r3.encoding='utf-8'
soup3=BeautifulSoup(r3.text,'html.parser')

list1=soup3.find_all('td')
list2=[]
for i in list1:
    list2.append(i.get_text())

i=5
while i < len(list2):
    with open(path,'a+',newline='') as f:
        csv_write=csv.writer(f)
        if list2[i]=='广西' or list2[i]=='新疆' or list2[i]=='宁夏':
            data_row=[college,year[1],list2[i]+'区',list2[i+2],list2[i+3],list2[i+4],contributor]
            csv_write.writerow(data_row)
        elif list2[i]=='内蒙古':
            data_row=[college,year[1],list2[i],list2[i+2],list2[i+3],list2[i+4],contributor]
            csv_write.writerow(data_row)
        elif list2[i]=='重庆':
            data_row=[college,year[1],list2[i]+'市',list2[i+2],list2[i+3],list2[i+4],contributor]
            csv_write.writerow(data_row)
        else:
            data_row=[college,year[1],list2[i]+'省',list2[i+2],list2[i+3],list2[i+4],contributor]
            csv_write.writerow(data_row)
        
    i=i+5
    
url4='http://zsjy.gzhu.edu.cn/info/1023/2052.htm'
r4=requests.get(url4,headers=headers1)
r4.encoding='utf-8'
soup4=BeautifulSoup(r4.text,'html.parser')

list1=soup4.find_all('td')
list2=[]
for i in list1:
    list2.append(i.get_text())

i=4
while i < len(list2):
    with open(path,'a+',newline='') as f:
        csv_write=csv.writer(f)
        data_row=[college,year[1],province,list2[i+1],list2[i],list2[i+2],contributor]
        csv_write.writerow(data_row)
    i=i+4
    
url5='http://zsjy.gzhu.edu.cn/info/1023/1724.htm'
r5=requests.get(url5,headers=headers1)
r5.encoding='utf-8'
soup5=BeautifulSoup(r5.text,'html.parser')

list1=soup5.find_all('td')
list2=[]
for i in list1:
    list2.append(i.get_text())

i=5
while i < len(list2):
    with open(path,'a+',newline='') as f:
        csv_write=csv.writer(f)
        if list2[i]=='广西' or list2[i]=='宁夏':
            data_row=[college,year[2],list2[i]+'区',list2[i+2],list2[i+1],list2[i+3],contributor]
            csv_write.writerow(data_row)
        elif list2[i]=='内蒙古':
            data_row=[college,year[2],list2[i],list2[i+2],list2[i+1],list2[i+3],contributor]
            csv_write.writerow(data_row)
        elif list2[i]=='重庆':
            data_row=[college,year[2],list2[i]+'市',list2[i+2],list2[i+1],list2[i+3],contributor]
            csv_write.writerow(data_row)
        elif list2[i]=='新疆普高':
            data_row=[college,year[2],'新疆区',list2[i+2],list2[i+1],list2[i+3],contributor]
            csv_write.writerow(data_row)
        else:
            data_row=[college,year[2],list2[i]+'省',list2[i+2],list2[i+1],list2[i+3],contributor]
            csv_write.writerow(data_row)
    i=i+5
    
url6='http://zsjy.gzhu.edu.cn/info/1023/2052.htm'
r6=requests.get(url6,headers=headers1)
r6.encoding='utf-8'
soup6=BeautifulSoup(r6.text,'html.parser')

list1=soup6.find_all('td')
list2=[]
for i in list1:
    list2.append(i.get_text())

i=4
while i < len(list2):
    with open(path,'a+',newline='') as f:
        csv_write=csv.writer(f)
        data_row=[college,year[2],province,list2[i+1],list2[i],list2[i+2],contributor]
        csv_write.writerow(data_row)
    i=i+4


