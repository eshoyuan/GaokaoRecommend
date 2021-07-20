# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:32:49 2020

@author: Mr.Lo
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://zsb.ecnu.edu.cn/webapp/scoreSearch-new2.jsp?id=2&pid='
years=['2017','2018','2019']     #年份
pids=['911','912','913','914','915','921','922','923','931','932','933','934','935','935','937','941','942','943','944','945','946','951','952','953','954',
     '961','962','963','964']    #省份编号
moduleId='&moduleId=31'

listData=[]   #存储爬取数据
for pid in pids:
    for year in years:
        url_request=url+pid+'&year='+year+moduleId
        r=requests.get(url_request,timeout=5)
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'html.parser')
        tr=(soup.find_all('tr'))
        for j in tr[1:]:         #tr2[1:]遍历第1列到最后一列，表头为第0列
            td = j.find_all('td')#td表格
            Year = td[0].get_text().strip()           
            Province = td[1].get_text().strip()  
            Batch = td[2].get_text().strip()            
            Category = td[3].get_text().strip()       
            Major= td[4].get_text()                     
            Score = td[5].get_text()                  
            listData.append([Year,Province,Batch,Category,Major,Score])
df=pd.DataFrame(listData,columns=['Year','Province','Batch','Category','Major','Score'])
df.insert(0,'College','华东师范大学')
df['Contributor']='09118134张立创'
df.drop('Batch',axis=1,inplace=True)
outputpath=r'D:\python上机\09119134张立创-华东师范大学.csv'
df.to_csv(outputpath,sep=',',index=False,header=True,encoding='gbk')