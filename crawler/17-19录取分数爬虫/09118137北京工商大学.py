#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='http://zsb.btbu.edu.cn/lqfs/lqfs2016/index.htm'
r=requests.get(url)
r.encoding='utf-8'


# In[2]:


print("获取省份页面列表")
sub_pages1=[];
start=1
i=1
while(r.text.find('点击右侧查看招生信息',start)!=-1):
    start=r.text.find('点击右侧查看招生信息',start)+1
    a=r.text.find("\"href\":\"",start)
    sub_page="http://zsb.btbu.edu.cn/lqfs/lqfs2016/"+r.text[a+8:r.text.find('htm',start)+3]
    sub_pages1.append(sub_page)
    print('\r'+str(int(100*i/34))+'%',end='  ')
    i+=1


# In[4]:


print("获取分数线页面列表")
sub_pages3=[];sub_pages4=[]
i=1
for page in sub_pages1:
    #print('\r'+str(int(100*i/len(sub_pages1)))+'%',end='  ')
    i+=1
    r=requests.get(page)
    r.encoding='utf-8'
    start=r.text.find("<div class=\"subPage\">")
    a=r.text.find("href",start)
    b=r.text.find("href",a+1)
    if a-start>100:
        continue  #排除港澳台，港澳台的页面异常
    sub1=r.text[a+6:r.text.find(".htm",a+6)+4]
    sub2=r.text[b+6:r.text.find(".htm",b+6)+4]
    sub_pages3.append(page[:-9]+sub1)
    sub_pages4.append(page[:-9]+sub2)


# In[5]:


print('获取分数线表格')
df_list1 = []
df_list2 = []
i=1
for page in sub_pages3:
    #print('\r'+str(int(100*i/len(sub_pages2)))+'%',end='  ')
    i=i+1
    res = requests.get(page)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    tables = soup.select('table')
    df_list1.append(pd.read_html(tables[0].prettify()))


# In[6]:


for i,page in enumerate(sub_pages4):
    #print('\r'+str(int(100*i/len(sub_pages2)))+'%',end='  ')
    i=i+1
    res = requests.get(page)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    tables = soup.select('table')
    if not pd.read_html(tables[0].prettify()):
        df_list2.append(pd.read_html(tables[1].prettify()))
    else:
        df_list2.append(pd.read_html(tables[0].prettify()))


# In[7]:


print('录入2019年数据')
output=pd.DataFrame(columns=['College','Year','Province','Category','Major','Score','Contributor'])
N=0
contributor='09118137岳元浩'
college='北京工商大学'
provinces=[]

for i in range(31): #遍历省
    province=None
    p0=df_list1[i][0][0][0].find('在')
    province=df_list1[i][0][0][0][p0+1:p0+3]
    j=0
    category='none'
    score=0
    major='none'
    #print(province,end="   ")
    if province is "内蒙":
        province="内蒙古"
    if province is "黑龙":
        province="黑龙江"
    provinces.append(province)
    for m in range(3,len(df_list1[i][0][j])):
            if '2019' in df_list1[i][0][3][1]:
                category=df_list1[i][0][2][m]
                score=df_list1[i][0][5][m]
                major=df_list1[i][0][1][m]
                year=2019#df_list[i][0][5][1][:4]
                #print('i='+str(i)+"  j="+str(j)+"   m="+str(m))
                if not pd.isnull(score) and category == "调档线" and major in ['文','理','综合改革','不分文理']:
                    category=major
                    major='all'
                    if category in ['综合改革','不分文理']:
                        category='all'
                    output.loc[N]={'College':college,'Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':contributor}
                    N+=1
                if not pd.isnull(score) and category in ['文','理','综合改革','不分文理']:
                    if category in ['综合改革','不分文理']:
                        category='all'
                    output.loc[N]={'College':college,'Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':contributor}
                    N+=1


# In[8]:


print('录入2017年数据')
#N=0
#output=pd.DataFrame(columns=['College','Year','Province','Category','Major','Score','Contributor'])
for i in range(31): #遍历省
    province=provinces[i]

    j=0
    category='none'
    score=0
    major='none'
    
    year=2017
    if i is 19:
        year=2018
    else:
        year=2017
    if i is 23 or i is 26 or i is 27 or i is 28:
        continue
    for m in range(3,len(df_list2[i][0][j])):
                category=df_list2[i][0][2][m]
                score=df_list2[i][0][5][m]
                major=df_list2[i][0][1][m]
                
                #df_list[i][0][5][1][:4]
                #print('i='+str(i)+"  j="+str(j)+"   m="+str(m))
                if score=='---':
                    score=None
                if score=='无':
                    score=None
                if  category == "调档线" and major in ['文','理','综合改革','不分文理']:
                    category=major
                    major='all'
                    if category in ['综合改革','不分文理']:
                        category='all'
                    output.loc[N]={'College':college,'Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':contributor}
                    N+=1
                if  category in ['文','理','综合改革','不分文理']:
                    if category in ['综合改革','不分文理']:
                        category='all'
                    output.loc[N]={'College':college,'Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':contributor}
                    N+=1


# In[9]:


print('录入2018年数据')
#N=0
#output=pd.DataFrame(columns=['College','Year','Province','Category','Major','Score','Contributor'])
for i in range(31): #遍历省
    province=provinces[i]
    j=0
    category='none'
    score=0
    major='none'
    
    if i is 19:
        continue#广东数据空缺
    #if i is 19 or i is 23 or i is 26 or i is 27 or i is 28:
        #continue
    for m in range(3,len(df_list2[i][0][j])):
                #print('i='+str(i)+"  j="+str(j)+"   m="+str(m))
                category=df_list2[i][0][2][m]
                if i is 6 or i is 0:
                    score=df_list2[i][0][10][m]
                elif i is 27:
                    score=df_list2[i][0][11][m]
                else:
                    score=df_list2[i][0][9][m]
                
                major=df_list2[i][0][1][m]
                year=2018#df_list[i][0][5][1][:4]
                
                if score=='---':
                    score=None
                if score=='无':
                    score=None
                if  category == "调档线" and major in ['文','理','综合改革','不分文理']:
                    category=major
                    major='all'
                    if category in ['综合改革','不分文理']:
                        category='all'
                    output.loc[N]={'College':college,'Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':contributor}
                    N+=1
                if  category in ['文','理','综合改革','不分文理']:
                    if category in ['综合改革','不分文理']:
                        category='all'
                    output.loc[N]={'College':college,'Year':year,'Province':province,'Category':category,'Major':major,'Score':score,'Contributor':contributor}
                    N+=1
#output.to_excel('excel版数据.xlsx')
output.to_csv('09118137岳元浩-北京工商大学.csv')
print('录入成功')


# In[ ]:


#df_list2[24][0][9][4]

