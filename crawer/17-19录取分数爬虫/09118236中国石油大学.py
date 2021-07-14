#!/usr/bin/env python
# coding: utf-8

# In[30]:


import requests        
import pandas as pd
import random
import json
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

url='https://zhaosheng.upc.edu.cn/f/cjcx'
Province = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆"]#所有有数据的省份
Year=['2019','2018','2017']
Category=['理工','文史']
info=pd.DataFrame(columns=['College', 'Year','Province','Category','Major','Score','Contributor'])


for year in Year:
    for province in Province:
        for cate in Category:
            
            Data={'ssmc':province,'zsnf':year,'klmc':cate,'zslx':'统招'}
            response = requests.post(url,data=Data,headers=request_headers)
            content = json.loads(response.text)
            for i in range(len(content['data']['sszygradeList'])):
                year=content['data']['sszygradeList'][i]['nf']
                province=content['data']['sszygradeList'][i]['ssmc']
                if (province=='上海')|(province=='浙江'):
                    category='综合改革'
                elif content['data']['sszygradeList'][i]['klmc']=='理工':
                    category='理科'
                else:
                    category='文科'
                major=content['data']['sszygradeList'][i]['zymc']
                score=content['data']['sszygradeList'][i]['minScore']
                information=information.append([{'College':'中国石油大学','Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':'09118215薛翔天'}])#增加一行新的数据
datacollection.to_csv('09118236廖滔-中国石油大学.csv',index=False)

   

