# -*- coding: utf-8 -*-
"""
Created on Thu May 21 08:11:34 2020

@author: Alexander
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup 
import re

def getScoreFrame(url,Year):
#传入形参url，Year（录取年份）
#使用pandas中的read_html()方法，将网站中的数据存入到DataFrame中
#并对DataFrame做一些删改，保留或添加上需要的信息
    r=requests.get(url)
    r.encoding='utf-8'
    df=pd.read_html(r.text)
    df_temp=pd.DataFrame(df[6].values[1:,:-2])
    if(Year=='2017'):
        if(url=='http://zs.dhu.edu.cn/f0/df/c14086a192735/page.htm'): #2017年浙江，无文理科一列
            df_temp.insert(3,"Category","无")
        
        df_temp.columns=["Province","unuseful","Major","Category","Score"]
        del df_temp["unuseful"]
        df_major=df_temp['Major']
        df_temp.drop('Major',axis=1,inplace=True)
        df_temp.insert(2,'Major',df_major)
        #df_temp[['Major','Category']]=df_temp[['Category','Major']]
    else:
        df_temp.columns=["Province","Category","unuseful","Major","Score"]  
        del df_temp["unuseful"]
    df_temp.insert(0,"College","东华大学")
    df_temp.insert(1,"Year",Year)
    df_temp["Contributor"]="09118136高成睿"
    df_temp.replace("总计","all",inplace=True)  #把总计改成all
    return df_temp

#获取所有子域名
page=['1','2','3']
Year=["2017","2018","2019"]
hrefBegin={"2017":"f0","2018":"38","2019":"a3"}
htmls=[[],[],[]]
for i,year in enumerate(Year):
    for p in page:
        r=requests.get("http://zs.dhu.edu.cn/"+year+"ngslqfscx/list"+p+".htm")
        pagesoup=BeautifulSoup(r.text,'lxml')
        for link  in pagesoup.find_all(attrs={"href":re.compile(r'^/'+hrefBegin.get(year))}):
            htmls[i].append(link.get('href'))

#将所有html中的录取信息表格存入到df_cont(DataFrame)中
flag=0
for i in range(3):
    for h in htmls[i]:
        url="http://zs.dhu.edu.cn"+h
        df_temp=getScoreFrame(url,Year[i])
        if(flag==0):
            df_cont=df_temp
            flag=1
        else:
            df_cont=pd.concat([df_cont,df_temp],axis=0)
df_cont.replace('\u200b',"all",inplace=True)  #全校分数可能在Major列为零长度字符串'\u200b'，替换为all
df_cont.fillna("all",inplace=True) #全校分数可能在Major列为空值，填充为all
#将df_cont存入.csv文件
df_cont.to_csv("./score of dhu.csv",index=False,header=True,encoding='gbk')