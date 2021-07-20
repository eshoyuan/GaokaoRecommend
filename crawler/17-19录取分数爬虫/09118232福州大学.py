# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:20:32 2020

@author: 12531
"""

import csv
import requests
from bs4 import BeautifulSoup


listData=[]#定义数组
listData.append(['College','Year','Province','Category','Major','Score','Contributor'])#写入表头



#2019年的数据
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}#爬虫[Requests设置请求头Headers],伪造浏览器
url= 'http://zsb.fzu.edu.cn/news/news_view.asp?news_id=2019102410114973499'
params = {"show_ram":1}
response = requests.get(url,params=params, headers=headers)#访问url
response.encoding='gbk'#该网页内容编码属性为gbk
soup = BeautifulSoup(response.text, 'html.parser')#获取网页源代码
tr = soup.find('table').find_all('tr')#.find定位到所需数据位置  .find_all查找所有的tr（表格）
College='福州大学'
Year='2019'
Province=''
Category=''
Contributor='09118232尹鑫龙'
for j in tr[2:-1]:        #tr2[2:-1]遍历第2行到倒数第2行，最后一行为多余行
    td = j.find_all('td')#td表格
    if len(td)==8:
        Province = td[0].get_text().strip()           
        Category = td[1].get_text().strip()  
        Major = td[2].get_text().strip()
        Score = td[5].get_text().strip()            
    else :
        Major = td[0].get_text().strip()
        Score = td[3].get_text().strip() 

    listData.append([College,Year,Province,Category,Major,Score,Contributor])




#2018年的数据
url= 'http://zsb.fzu.edu.cn/news/news_view.asp?news_id=2018921545073499'
response= requests.get(url,params=params, headers=headers)#访问url
response.encoding='gbk'
soup = BeautifulSoup(response.text, 'html.parser')
tr = soup.find('table').find_all('tr')
Year='2018'
for j in tr[2:-1]:        
    td = j.find_all('td')
    if len(td)==8:
        Province = td[0].get_text().strip()         
        Category = td[1].get_text().strip()  
        Major = td[2].get_text().strip()
        Score = td[5].get_text().strip()        
    else :
        Major = td[0].get_text().strip()
        Score = td[3].get_text().strip() 

    listData.append([College,Year,Province,Category,Major,Score,Contributor])
    
    
    
#2017年的数据
url= 'http://zsb.fzu.edu.cn/news/news_view.asp?news_id=201792911284473499'
response= requests.get(url,params=params, headers=headers)#访问url
response.encoding='gbk'
soup = BeautifulSoup(response.text, 'html.parser')
tr = soup.find('table').find_all('tr')
Year='2017'
for j in tr[2:-1]:        
    td = j.find_all('td')
    if len(td)==8:
        Province = td[0].get_text().strip()         
        Category = td[1].get_text().strip()  
        Major = td[2].get_text().strip()
        Score = td[5].get_text().strip()        
    else :
        Major = td[0].get_text().strip()
        Score = td[3].get_text().strip() 

    listData.append([College,Year,Province,Category,Major,Score,Contributor])
    
    
#存入csv文件
with open('09118232尹鑫龙-福州大学.csv', 'w+', newline='',encoding='gbk') as f:
    write=csv.writer(f)
    write.writerows(listData)
