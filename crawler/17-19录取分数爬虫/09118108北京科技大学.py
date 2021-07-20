# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:52:17 2020

@author: 21318
"""

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import pandas as pd

#省份代码，用于爬取静态网页，相当于爬取了固定的31*2个网址
Province=["110000","120000","130000","140000","150000","210000","220000",
          "230000","310000","320000","330000","340000","350000","360000",
          "370000","410000","420000","430000","440000","450000","460000",
          "500000","510000","520000","530000","540000","610000","620000",
          "630000","640000","650000"]
#在后面存储时，将省份的信息填入
ProvinceChinese=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海',
                 '江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东',
                 '广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海',
                 '宁夏','新疆']
#理工科为1，文史科为2
Subject=['1','2']
#k数组用来存储直接爬取到的结果
k=[]
#u数组存储能转化为csv格式的结果
u=[]

for i in Province:
    for j in Subject:
        #先获取网址
        l='http://zhaosheng.ustb.edu.cn/front/zs/toMark.jspa?provinceId='+str(i)+'&subjectId='+str(j)
        print(l)
        #爬取并解析和存储
        response = urlopen(l)
        soup=bs(response.read(),'html.parser')
        items=soup.find_all('td')
        for o in items:
            k.append(o.string)
#去除无用信息如制表符之类           
for i in range(len(k)):
    k[i]=k[i].strip('\r\n/\r\n               \t\t      ')
#将爬取到的信息转化为易于csv存储的格式    
for m in range(3):
    for i in range(len(k)):
        if i%6==0:
            if k[i+1]=='理工' or k[i+1]=='文史':
                u.append(['北京科技大学',2017+m,'北京',k[i+1][0]+'科',k[i],k[i+3+m][4:],'09118108朱佳涛'])
#加入省份信息
times=1#用于计数存储省份信息
for i in range(1,len(u)//3):
    if u[i][3]=='理科' and u[i-1][3]=='文科':
        for k in range(i,len(u)//3):
            u[k][2]=ProvinceChinese[times]
            u[k+len(u)//3][2]=ProvinceChinese[times]
            u[k+2*len(u)//3][2]=ProvinceChinese[times]
        times+=1
        
#转化为csv格式存储    
csv_list = pd.DataFrame(columns=['College','Year','Province','Category','Major','Score','Contributor'],data=u)
csv_list.to_csv('xy.csv', encoding='gbk')

















