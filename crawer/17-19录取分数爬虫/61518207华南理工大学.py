#!/usr/bin/env python
# coding: utf-8

# In[246]:


from bs4 import BeautifulSoup
from urllib import request
import pandas as pd


# In[247]:


LinkList=['https://admission.scut.edu.cn/2019/0708/c17520a327240/page.htm',
         'https://admission.scut.edu.cn/2018/0712/c17520a292387/page.htm',
         'https://admission.scut.edu.cn/2017/0711/c17520a292381/page.htm']             #三年录取分数线的链接表


# In[248]:


college=[]      #'华南理工大学
year=[]         #
province=[]
category=[]
major=[]        #'all
score=[]
contributor=[]  #'61518207张政
i=2020
j=0           #由于17年表格不同于18，19，设置j,l为提取信息时的index偏移量
l=0
for link in LinkList:
    i=i-1
    print(i)
    url = link
    html=request.urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    if i==2017:   #设置index偏移
        j=2
        l=1
    for trs in soup.find_all("tr")[1+1:-1:]:   #首列为表头，为无效信息
        tds=trs.find_all('td')
        if len(tds)==9:
            college.append('华南理工大学')
            major.append('all')
            contributor.append('61518207张政')
            year.append(i)
            province.append(tds[0].string.strip('\t'))
            #if (tds[1].string.strip('\t')!='文' and  tds[1].string.strip('\t')!='理'):
               # category.append('all')
            #else:
            category.append(tds[1].string.strip('\t'))
            score.append(tds[5+j].string.strip('\t'))
        elif len(tds)==8:
            college.append('华南理工大学')
            major.append('all')
            contributor.append('61518207张政')
            year.append(i)
            province.append(province[-1])
            #if (tds[0].string.strip('\t')!='文' and  tds[0].string.strip('\t')!='理'):
               # category.append('all')
            #else:
            category.append(tds[0].string.strip('\t'))
            score.append(tds[4+j].string.strip('\t'))


# In[249]:


temp={"College":college,"Year":year,"Province":province,"Category":category,"Major":major,"Score":score,"Contributor":contributor}


# In[250]:


data=pd.DataFrame(temp)


# In[253]:


outputpath='E:/2020春季学期/软件实践/61518207张政-华南理工大学.csv'
data.to_csv(outputpath,sep=',',index=False,header='College,Year,Province,Category,Major，Score，Contributor')

