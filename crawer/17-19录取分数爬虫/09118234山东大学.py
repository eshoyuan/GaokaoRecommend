#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd 


# In[2]:


province_list=['黑龙江','吉林','辽宁','内蒙古','山东','河北','北京','江苏','浙江','福建','安徽','广东','广西','云南','贵州','四川','重庆','湖北','湖南','山西','陕西','宁夏','甘肃','青海','新疆','西藏','上海','江西','香港','澳门','台湾']
subject_list=['理工','文史']
year_list=['2019','2018','2017']
kind_list=['普通类','高校专项','国家专项']
url='http://www.bkzssys.sdu.edu.cn/f/ajax_lnfs?ts=1588909808236'


# In[3]:


def get_source(url='http://www.bkzssys.sdu.edu.cn/f/ajax_lnfs?ts=1588909808236',province='山西',year='2018',subject='理工',kind='普通类'):
    data={'ssmc': province,
    'zsnf': year,
    'klmc': subject,
    'zslx': kind}
    response = requests.post(url, data=data)
    if(response.json()['state']):
        source=response.json()['data']['sszygradeList']
    else:
        print(f'{year}{province}没有报考山东大学{subject}的{kind}考生')
        empty=[]
        return empty
    return source


# In[4]:


target_list=['nf','klmc','ssmc','zymc','minScore','minOrder']
def get_header(source,target_list=['nf','klmc','ssmc','zymc','minScore','minOrder']):#获得df的头#参数为目标头的合集
    df={}
    for item in source[0]:
        if item in target_list:
            df[item]=source[0][item]
    tdf=pd.DataFrame(df,index=[0])
    return tdf
def header(target_list=['nf','klmc','ssmc','zymc','minScore','minOrder']):
    result =pd.DataFrame(columns=target_list)
    return result


# In[5]:


def source_to_df(source,tdf=None):#tdf为以前的df，没有则置位开始的头
    if tdf==None:
        tdf=header()#获得头
    df={}
    for i in range(len(source)):
        for item in source[i]:
            if item in target_list:
                df[item]=source[i][item]
        tdf=tdf.append(df,ignore_index=True)
        
    return tdf


# In[6]:


def save_as_csv(df,save_path='D:\大二下学期课程\软件实践\爬虫3.csv'):
    df.to_csv(save_path,encoding='utf_8_sig')


# In[7]:
all_source=[]
all_df=[]
for province in province_list:
    for subject in subject_list:
        for year in year_list:
                all_source.append(get_source(province=province,subject=subject,year=year))
tdf=header()#获得头               
for item in all_source:
    tdf=tdf.append(source_to_df(item),ignore_index=True)
save_as_csv(tdf)


