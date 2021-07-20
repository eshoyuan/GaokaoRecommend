import requests
from bs4 import BeautifulSoup
import csv

def getURL(url):
    # 获取html信息并找到相关标签
    URL=list()
    time=list()
    TYPE=list()
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    for ul in soup.select('a'):
        if(str(ul)[75:90]!="" and str(ul)[75]!="a" and str(ul)[77]=="1" and int(str(ul)[78])>6):
            URL.append("http://zs.wust.edu.cn/bk/"+str(ul)[9:29])
            time.append(int(str(ul)[75:79]))
            TYPE.append(str(ul)[86:89])
    return URL,time,TYPE
    # 获取专业及分数等数据

def GetInfo(url,time):
    print(time)
    print(url)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    table=soup.find_all("table")
    #print(table)
    x=list()
    for j in table:
        td=j.select('td')
        #print(td)
        for k in td:
            #print(k.attrs)
            y=k.text.strip()
            if(y!="" and len(y)<5):
                x.append(y)
    province = ['浙江','安徽','北京','福建','甘肃','港澳台',                   
             '广东','广西','贵州','海南','河南','河北',
             '黑龙江','湖北','湖南','江苏','江西','辽宁',
             '内蒙古','宁夏','青海','山东','山西','陕西',
             '上海','四川','西藏','新疆','云南','重庆','天津','吉林']
    info=list()
    temp=list()
    i=0
    for item in x:
        if item in province:
            info.append(temp)
            temp=list()
        temp.append(item)
    info.append(temp)
    info.remove(info[0])
    #print(info)
    value=list()
    for item in info:
        if(len(item)>6):
            value.append(["武汉科技大学",time,item[0],"理科","-",item[4],"61518421栾岱洋"])
            value.append(["武汉科技大学",time,item[0],"文科","-",item[8],"61518421栾岱洋"])
        else:
            if(item[1]=="不分文理"):
                value.append(["武汉科技大学",time,item[0],"不分文理","-",item[-1],"61518421栾岱洋"])
            else:
                value.append(["武汉科技大学",time,item[0],"理科","-",item[4],"61518421栾岱洋"])
    return value
            
        

    
url="http://zs.wust.edu.cn/bk/Category.aspx?ID=6"
URL,time,TYPE=getURL(url)
myTable=list()
for i in range(len(URL)):
    if(TYPE[i]=="）高考"):
        for item in GetInfo(URL[i],time[i]):   
            myTable.append(item)
    
#print(myTable)


import pandas as pd

name=['College','Year','Province','Category','Major','Score','Contributor']
test=pd.DataFrame(columns=name,data=myTable)#数据有三列，列名分别为one,two,three
print(test)
test.to_csv('61518421 栾岱洋-武汉科技大学.csv',encoding='gbk')

