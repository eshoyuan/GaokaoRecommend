# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:52:07 2020

@author: Jingting Wang
"""

from bs4 import BeautifulSoup  
import requests  
import csv   
 
#检查url地址  
def check_link(url):  
    try:  
        r = requests.get(url)  
        r.encoding = 'utf-8' 
        return r.text
    except:  
        print('无法链接服务器！！！')  
        
#爬取资源  
def get_contents(rurl):    
    ulist =  []    #存储爬取到的该年的数据
    soup = BeautifulSoup(rurl,'html.parser')  
    tbody = soup.find('tbody')   #信息表格在<tbody>标签中 
    trs=tbody.find_all('tr')  #<tr>为表格中的每一行
    for index,tr in enumerate(trs):
        if(index>=2):   #tr[2]之前为表头信息,所以从tr[2]开始爬取
            ui=[]   #存储该行内容
            spans = tr.find_all('span')   #表格中的数据在<span>标签中，找到该行所有的<span>
            for span in spans:  
                ui.append(span.get_text()[:4])  #获取该行<span>标签中的内容
            if(ui[0]=='西藏'):   #由于西藏一行各年的标签设置方式不同，在此将其统一，方便之后操作
                uj=[ui[0],ui[1],ui[3][:3]]
                ulist.append(uj)
            else:
                ulist.append(ui)
    return ulist

#处理爬取到的数据，统一形式,以便写入csv文件
def formation(year_list,year,result_list): #year_list为爬取到的该年的数据 year为年份 result_list为三年数据
    for prov in year_list:   #遍历该年各省份
        if(prov[0]=='上海')or(prov[0]=='浙江'):
            item1 = ['上海交通大学',year,prov[0],'all','校本部',prov[2],'09118140王靖婷']    #格式化后的列表
            item2 = ['上海交通大学',year,prov[0],'all','医学院',prov[3],'09118140王靖婷']
            result_list.extend([item1,item2])
        elif(prov[0]=='港澳台侨')or(prov[0]=='西藏'):
            if(prov[0]=='港澳台侨')and(year=='2018'):   #港澳台侨2018年数据与其他两年有所不同需单独处理
                item = ['上海交通大学',year,prov[0],'all','all',prov[3],'09118140王靖婷']
            else:
                item = ['上海交通大学',year,prov[0],'all','all',prov[2],'09118140王靖婷']
            result_list.append(item)
        else:
            item1 = ['上海交通大学',year,prov[0],'理科','校本部',prov[2],'09118140王靖婷']
            item2 = ['上海交通大学',year,prov[0],'文科','校本部',prov[3],'09118140王靖婷']
            item3 = ['上海交通大学',year,prov[0],'理科','医学院',prov[4],'09118140王靖婷']
            result_list.extend([item1,item2,item3])
    return result_list
 


           
url19 = "https://zsb.sjtu.edu.cn/web/jdzsb/3810062-3810000002538.htm?Page=1"
url18 = 'https://zsb.sjtu.edu.cn/web/jdzsb/3810062-3810000002172.htm?Page=2&BJ=0'
url17 = 'https://zsb.sjtu.edu.cn/web/jdzsb/3810062-3810000001785.htm?Page=3&BJ=0'

url = [url19,url18,url17]   #要爬取的地址
year = ['2019','2018','2017']   #相应的年份
result = []  #最终写入文件的列表数据

#爬取各年的数据
for i in range(3):
    rs = check_link(url[i])  #检查url地址
    y_list = get_contents(rs)   #爬取内容
    formation(y_list,year[i],result)   #处理数据

#写入文件"09118140王靖婷-上海交通大学.csv"
with open("09118140王靖婷-上海交通大学.csv",'w',newline='' "") as f:  
    writer = csv.writer(f)   
    writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])  #写入表头
    writer.writerows(result)  #写入数据