# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:44:17 2020

@author: 28321
"""
##由于官方网站不提供各专业的文理的单独分数线，所以分类中不存在文理
##而2017年，2018年，2019年三年的网站形式不同，分别攥写了各自针对他们的函数进行爬取
import requests
import pandas as pd
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):##读取网站信息
    try:
        hd={'user-agent':'Chrome/10'}
        r=requests.request('GET',url,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
    
def fillList2019(ulist,html): #针对2019年各专业录取分数线读取
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            if len(tds)==4:
                ulist.append(['2019',tds[0].string,tds[1].string,tds[2].string,tds[3].string])
  
def fillList2018(ulist,html):  #针对2018年各专业录取分数线读取
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            if len(tds)==4:
                ulist.append(['2018',tds[0].string,tds[1].string,tds[2].string,tds[3].string])          
                
def fillList2017(ulist,html):  #针对2017年各专业录取分数线读取
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            if len(tds)==3:
                ulist.append(['2017',tds[0].string,tds[1].string,tds[2].string])                         
                
            
def printList(ulist):   #打印2019，2018年各专业分数线
    for i in range(len(ulist)):
        u=ulist[i]
        print("{:^10}\t{:^10}\t{:^20}\t{:^10}\t{:^10}".format(u[0],u[1],u[2],u[3],u[4]))
        
def printList2017(ulist):   #打印2017年各专业分数线  
    for i in range(len(ulist)):
        u=ulist[i]
        print("{:^10}\t{:^10}\t{:^20}\t{:^10}".format(u[0],u[1],u[2],u[3]))      

url2019='https://zsb.seu.edu.cn/2019/0905/c23657a285002/page.htm'
url2018='https://zsb.seu.edu.cn/2019/0119/c23657a262237/page.htm'
url2017='https://zsb.seu.edu.cn/2018/0315/c23657a209629/page.htm'

uinfo=[]
uinfo2017=[]
uinfo2018=[]
uinfo2019=[]
##先读取2019年高考各专业分数线
html2019=getHTMLText(url2019)
fillList2019(uinfo2019,html2019)
printList(uinfo2019)

##读取2018年高考各专业分数线
html2018=getHTMLText(url2018)
fillList2018(uinfo2018,html2018)
printList(uinfo2018)

##读取2017各专业高考分数线
html2017=getHTMLText(url2017)
fillList2017(uinfo2017,html2017)
printList2017(uinfo2017)

uinfo.extend(uinfo2019)
uinfo.extend(uinfo2018)
uinfo.extend(uinfo2017)
test=pd.DataFrame(data=uinfo)  
test.to_csv('d:/各年份各专业分数.XLS')##保存在表格文件中

    