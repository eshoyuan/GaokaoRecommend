# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:26:49 2020

@author: 12921
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd

url='http://zb.cumtb.edu.cn/f/ajax_lnfs?ts=1589432375473'#数据准备
Year=['2019','2018','2017']
Province=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北',
          '湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆','台湾','香港','澳门']
Category=['理工','文史']

graph_property={'Year':[],'Province':[],'Category':[],'Major':[],'Score':[]}#建立表头
data=pd.DataFrame(graph_property)

#爬取数据
for i in Year:
    for j in Category:
        for k in Province:
            #打印正在爬取的数据
            print(i,j,k)
            form_data={'ssmc': k,'zsnf': i,'klmc': j,'zslx': '普通生'}
            response = requests.post(url,data=form_data)
            content = json.loads(response.text)
            info=pd.DataFrame(content['data'][ 'sszygradeList'])
            #跳过没有数据的条件
            if(info.size==0):
                continue
            less_info=info[['nf','ssmc','klmc','zymc','minScore']]
            if(j=='理工'):
                less_info['klmc']='理科'
            else:
                less_info['klmc']='文科'
            less_info.columns=['Year','Province','Category','Major','Score']
            data=data.append(less_info)
            
print('爬取成功！总共',data.shape[0],'条记录。')            
data.insert(0,'College','中国矿业大学（北京）')
data['Contributor']='09118121闻浩'
file_path='09118121闻浩-中国矿业大学（北京）.csv'
data.to_csv(file_path,index=False)