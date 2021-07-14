# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:04:43 2020

@author: Yuwei Xu
"""
from bs4 import BeautifulSoup 
import requests 
import csv 
  
#爬取资源 
def get_contents(ulist,text,model): 
    soup = BeautifulSoup(text,'lxml') 
    trs = soup.find_all(model) 
    for tr in trs: 
        ui = [] 
        for td in tr: 
            ui.append(td.string) 
        ulist.append(ui) 
   
#保存资源 
def save_contents(urlist,model,year): 
    with open("61518110徐昱玮-中南大学.csv",'a') as f: 
        writer = csv.writer(f,lineterminator='\n') 
        temp_row= ['' for _ in range(11)]
        if(model=='td'):
            k=14
        elif(model=='p'):
            k=0
        else:
            print('ERROR!!!!')
        for i in range(32):
            for _ in range(11):
                temp_row[_] = urlist[k][1]
                if(urlist[k][1]=='\u2003'):
                    temp_row[_]='————'
                k=k+1
            writer.writerow(['中南大学',year,temp_row[0],'理科','All',temp_row[4],'61518110徐昱玮'])
            writer.writerow(['中南大学',year,temp_row[0],'文科','All',temp_row[9],'61518110徐昱玮'])
    
def crawler(url,model,year):
    urli = [] 
    text = requests.get(url).text
    get_contents(urli,text,model) 
    save_contents(urli,model,year) 

with open("61518110徐昱玮-中南大学.csv",'w') as f: 
    writer = csv.writer(f,lineterminator='\n') 
    writer.writerow(['中南大学录取分数'])
    writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])
url_2019 = "http://zhaosheng.csu.edu.cn/admitline.aspx?nid=2277"
url_2018 = "http://zhaosheng.csu.edu.cn/admitline.aspx?nid=2070"
url_2017 = "http://zhaosheng.csu.edu.cn/admitline.aspx?nid=1818"
crawler(url_2019,'td','2019')
crawler(url_2018,'p','2018')
crawler(url_2017,'td','2017')
print('写入完成')