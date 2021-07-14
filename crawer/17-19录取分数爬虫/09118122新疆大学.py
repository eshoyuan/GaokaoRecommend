# -*- coding: utf-8 -*-
import requests 
import pandas as pd
import json

#设置动态js的url
url = 'http://welcome.xju.edu.cn/Web/Home/GetRecordScore'
#设置url post请求的参数
data={}
year=['2018','2019']
ss=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']

List=[]

for i in year:
    data['NowYear']=i
    for j in ss:
        data['OmitName']=j
        req=requests.post(url,data=data)
        req = json.loads(req.text)
        for x in req:
            if x['LQPC']!='本科一批次':
                continue
            temprow={'College':"新疆大学",'Contributor':'09118122邵一展'}
            temprow['Year']=i
            temprow['Province']=j
            temprow['Major']=x['SpecialtyName'] if x['SpecialtyName']!=None else 'All'
            temprow['Score']=x['MinScore']
            temprow['Category']=x['SpeType'] if x['SpeType']!='不分文理' else 'All'
            List.append(temprow)

df = pd.DataFrame(List,columns=['College','Year','Province','Category','Major','Score','Contributor'])
df.to_csv("09118122邵一展-新疆大学.csv",index=False,sep=',',encoding='utf-8-sig')