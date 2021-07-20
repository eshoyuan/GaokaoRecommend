# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:06:55 2020

@author: XUYONG
"""

import requests 
from bs4 import BeautifulSoup
import re
from w3lib.html import remove_tags
import csv
import pandas as pd
 
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
ALL=[]
url='https://zsb.jnu.edu.cn/88/df/c4292a428255/page.htm'
req=requests.get(url,headers=headers,timeout=3)
res=req.content
soup=BeautifulSoup(res,'lxml')###获取网页内容

s=soup.select('td')
text=[]
for i in s:
    stri=str(i)
    stri = re.sub(u"\\<.*?\\>", "", stri)
    stri=re.sub("\xa0", "", stri)
    text.append(stri)

for j in range(len(text)):###找到表格的开始
    if text[j]=="平均分超出分数线":
        m1=j
        break

n1=(len(text)-m1)//10###循环次数



province1=[]###省份
batchtype1=[]###批次类型
batch=[]###批次
subject1=[]###文理科
admission=[]###录取人数
yiben=[]###一本线
maxg=[]###最高分
ming1=[]###最低分
avg=[]###均分
overavg=[]###平均分超过一本线


for k in range(n1):
    province1.append(text[m1+1])
    batchtype1.append(text[m1+2])
    batch.append(text[m1+3])
    subject1.append(text[m1+4])
    admission.append(text[m1+5])
    yiben.append(text[m1+6])
    maxg.append(text[m1+7])
    ming1.append(text[m1+8])
    avg.append(text[m1+9])
    overavg.append(text[m1+10])
    m1=m1+10

for k in range(n1):
    province1[k]=province1[k],batchtype1[k]




###完成2019年的爬取

url='https://zsb.jnu.edu.cn/12/2c/c4292a266796/page.htm'
req=requests.get(url,headers=headers,timeout=3)
res=req.content
soup=BeautifulSoup(res,'lxml')###获取网页内容

s=soup.select('td')
text=[]
for i in s:
    stri=str(i)
    stri = re.sub(u"\\<.*?\\>", "", stri)
    stri=re.sub("\xa0", "", stri)
    text.append(stri)

for j in range(len(text)):###找到表格的开始
    if text[j]=="平均分超分数线":
        m2=j
        break

n2=(len(text)-m2)//10###循环次数



province2=[]###省份
batchtype2=[]###批次类型
batch=[]###批次
subject2=[]###文理科
admission=[]###录取人数
yiben=[]###一本线
maxg=[]###最高分
ming2=[]###最低分
avg=[]###均分
overavg=[]###平均分超过一本线


for k in range(n2):
    province2.append(text[m2+1])
    batchtype2.append(text[m2+2])
    batch.append(text[m2+3])
    subject2.append(text[m2+4])
    admission.append(text[m2+5])
    yiben.append(text[m2+6])
    maxg.append(text[m2+7])
    ming2.append(text[m2+8])
    avg.append(text[m2+9])
    overavg.append(text[m2+10])
    m2=m2+10

for k in range(n2):
    province2[k]=province2[k],batchtype2[k]

    
###完成2018数据爬取

url='https://zsb.jnu.edu.cn/70/ec/c4292a159980/page.htm'
req=requests.get(url,headers=headers,timeout=3)
res=req.content
soup=BeautifulSoup(res,'lxml')###获取网页内容

s=soup.select('td')
text=[]
for i in s:
    stri=str(i)
    stri = re.sub(u"\\<.*?\\>", "", stri)
    stri=re.sub("\xa0", "", stri)
    text.append(stri)

for j in range(len(text)):###找到表格的开始
    if text[j]=="平均超出一本线":
        m3=j
        break

n3=(len(text)-m3)//9###循环次数



province3=[]###省份
batchtype3=[]###批次类型
batch=[]###批次
subject3=[]###文理科
admission=[]###录取人数
yiben=[]###一本线
maxg=[]###最高分
ming3=[]###最低分
avg=[]###均分
overavg=[]###平均分超过一本线


for k in range(n3):
    province3.append(text[m3+1])
    batchtype3.append(text[m3+2])
    batch.append(text[m3+3])
    subject3.append(text[m3+3])
    admission.append(text[m3+4])
    yiben.append(text[m3+5])
    maxg.append(text[m3+6])
    ming3.append(text[m3+7])
    avg.append(text[m3+8])
    overavg.append(text[m3+9])
    m3=m3+9

for k in range(n3):
    province3[k]=province3[k],batchtype3[k]
###完成2017数据爬取

###构建csv
Major=["All"]*(n1+n2+n3)
College=["暨南大学"]*(n1+n2+n3)
Contributor=["徐志修"]*(n1+n2+n3)
Year=["2019"]*n1+["2018"]*n2+["2017"]*n3
province=province1+province2+province3
subject=subject1+subject2+subject3
ming=ming1+ming2+ming3
dataframe=pd.DataFrame({"Collega":College,"Year":Year,"Province":province,"Category":subject,"Major":Major,"Score":ming,"Contributor":Contributor})
dataframe.to_csv("testcollege.csv")