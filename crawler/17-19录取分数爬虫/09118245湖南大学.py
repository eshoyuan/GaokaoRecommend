# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:08:59 2020

@author: Chen
"""


'''
说明：
*：需要引用资源文件“uapools.py”，里面是getpage所使用的ua池,如果不使用默认的用户代理池可以在ua函数中的默认值uapool处修改成自定义的用户代理池
1.getpage用于获取网页源代码，getinfo从含表格的网页提取信息
2.源网页需要填写表单，但实际上网页是通过用户填入的信息来改变在表单部分下得网页链接，所以可以根据网页链接的规律
直接访问下方链接。所以程序中没有出现填写表单的操作。
'''
#载入软件包=====================================
#数据结构
import pandas as pd
import numpy
#爬虫操作
import urllib as url
import urllib.request as urlr
import urllib.error as urle
import urllib.parse as urlp

import urllib3#有些网站需要使用urllib3

#常用模组
import random as rand
import re
import time
import sys

#csv读写
import csv
import codecs
#================================================
#载入资源文件uapools.py
from uapools import uapools
print("载入成功")

coding='UTF-8'

def ua(muapools=uapools,method=0):#传入资源列表中的uapools，里面有1499个标签值可使用
    thisua=rand.choice(muapools)#从uapools中随机使用一个
    #print("当前使用的用户为："+thisua)
    headers=("User-Agent",thisua)#用元组的形式制作头信息，（标签，用户名）
    opener=urlr.build_opener()#使用urlr.build_opener()来获取总的内容
    opener.addheaders=[headers]#添加用户信息
    urlr.install_opener(opener)#安装为全局
def getpage(url,method=0):#ippoolsurl代表接口网址，url代表目标网址
    file=""
    if(method==0):#默认使用urllib方法
        for counts in range(0,9):
            try:
                ua()
                file=urlr.urlopen(url).read().decode('UTF-8',"ignore")
                break
            except urle.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
        print("爬取成功")
    elif(method==1):#有的时候我们需要使用urllib3的方法
        for counts in range(0,9):
            try:
                http = urllib3.PoolManager()
                thisua=rand.choice(uapools)#从uapools中随机使用一个
                #print("当前使用的用户为："+thisua)
                headers={"User-Agent":thisua}#用字典的形式制作头信息，（标签，用户名）
                r=http.request('GET',url,headers=headers)
                file=(r.data).decode('UTF-8','ignore')
                break
            except urle.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
    return file

def getinfo(file):
    pat=pat='{"klmc":"(.*?)","pjf":.*?,"sfmc":"(.*?)","year":"(.*?)","zdf":(.*?),"zgf":.*?,"zymc":"(.*?)"}'
    rst=re.compile(pat).findall(file)
    info=[]
    for i in range(0,len(rst)):
        sinfo=['湖南大学',rst[i][2],rst[i][1]]#一条信息
        if(rst[i][0]=='普通(文)'):
            sinfo.append('文科')
        elif(rst[i][0]=='普通(理)'):
            sinfo.append('理科')
        else:
            sinfo.append(rst[i][0])
        sinfo.extend([rst[i][4],rst[i][3],'09118245陈品多'])
        info.append(sinfo)
    return info

#从查询网页获取省份
pat='<option value="([^\d].*?)">(.*?)</option>'#匹配一个字符串，字符串满足前一项要匹配的内容的第一个字符不是数字
query_file=getpage('http://admi.hnu.cn/zsxt2/lnlqqk')
provinces_raw=re.compile(pat).findall(query_file)
provinces=[]
for elem in provinces_raw:#筛选
    if elem[0]==elem[1]:
        provinces.append(urlr.quote(elem[0]))#网页中含有省份名称的标签满足标签内容和标签名称相等

years=['2019','2018','2017','2016']

info=[]#存储信息

for year in years:
    for province in provinces:
        time.sleep(1)
        file=getpage('http://admi.hnu.cn/zsxt2/lnlqqkSearch?year='+year+'&'+'sf='+province)
        info.extend(getinfo(file))
print('爬取完毕')

csv_file = codecs.open('09118245陈品多-湖南大学.csv','w','gbk')
writer = csv.writer(csv_file)
writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])
for elem in info:
    writer.writerow(elem)
csv_file.close()
print('运行完毕')
