# -*- coding: utf-8 -*-

import requests
import openpyxl
from bs4 import BeautifulSoup


url = "http://zsxx.njau.edu.cn/lnlqfs.jsp?wbtreeid=1024"
year = [2019,2018,2017]
prov = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','河北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
wb=openpyxl.Workbook()
sheet=wb.active
list1 = []
data = []
name = '南京农业大学'


contributer = '09118225李璟宸'
'''1.得到网页中td的分数线数据 '''
def getList(soup):
    list=[]
    data=soup.find_all('tr')
    for tr in data:
        ltd=tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv=[]
        for td in ltd:
            singleUniv.append(td.string)
        list.append(singleUniv)
    return list
''' 2.根据年份和省份得到关于分数线的列表 '''     
def find(year,prov):
    data={'nf':year,'sf':prov}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    res = requests.post(url = url,data=data,headers= headers)
    res.encoding='UTF-8'
    html1 = res.text
    soup=BeautifulSoup(html1,"html.parser")
    return getList(soup)




'''3.根据省份和年份列表得到整体列表 '''
for i in range(3):
    for j in range(31):
        list1 = find(year[i],prov[j])       
        for u in list1[1:]:
            data.append([name,year[i],prov[j],u[1],u[0],u[3],contributer])

''' 4.文件处理操作'''
list2 = ['College','Year','Province','Category','Major','Score','Contributer']
data.insert(0,list2)
for each in data:
    sheet.append(each)
wb.save('D://3.csv')

