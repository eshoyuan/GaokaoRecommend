#!/usr/bin/env python
# coding: utf-8

# In[215]:


import requests
from bs4 import BeautifulSoup
import re
import csv


# In[216]:


#设置基本的常数

contributor = '09118110白劭宸'
college = '北京邮电大学'

url = 'https://zsb.bupt.edu.cn/'
append = 'list/list.php?p=5_5'


# In[218]:


pages = ['1','2','3']  #用来切换不同界面


# In[213]:


def get_data(url):  #得到url后获取网页大纲内容
    strhtml = requests.get(url)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    
    data = soup.select('body > div.mar0a.grd25.wrap.bagf.ovhi > div.list_bg > div.list.rt.grd20 > ul > li > a')
    
    return data


# In[222]:


def get_page_table(data):  #得到网页那日容后，获取表格内容，并写入

    for item in data:

        txt = item.get_text()[10::]
        flag = txt.find('—')

        if flag == -1:
            continue

        province = txt[flag+2:-1:]
        year = ''.join(re.findall('\d',txt))

        #print(item)

        strhtml = requests.get(url+item.get('href'))
        strhtml.encoding = 'utf-8'
        soup=BeautifulSoup(strhtml.text,'html.parser')

        tr = soup.find_all('tr')
        category = '理科'

        for j in tr[1:-1]:
            td = j.find_all('td')#td表格
            major = td[0].get_text().strip()
        
            if major.find('总计（中外合作办学专业）') != -1:
                category = '文科'
                continue
                
            if major.find('总计') != -1:
                continue

            score = td[3].get_text()

            csv_write.writerow([college,year,province,category,major,score,contributor])
            #print(college,year,province,category,major,score,contributor)
            
    return


# In[223]:


#打开文件并写入文件的表头

f = open('09118110白劭宸-北京邮电大学.csv','w',encoding='utf-8-sig',newline='')

csv_write = csv.writer(f,dialect='excel')
csv_write.writerow(['College','Year','Province','Category','Major','Score','Contributor'])


# In[224]:


#遍历所有需要的爬取的网页链接

for i in pages[-1::-1]:    
    for j in pages:
    
        data = get_data(url+append+i+'_'+j)
        
        get_page_table(data)


# In[ ]:




