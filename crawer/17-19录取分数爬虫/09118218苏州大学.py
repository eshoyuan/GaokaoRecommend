# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:02:57 2020

@author: 墨湘灵
"""

import requests
import re

def getHTMLText(url):

    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
#异常处理
    except:
        return "产生异常"


def parse_one_page(html):

    res='<font.*?>(.*?)<.*?/font>'
    page1=re.sub('<a.*?=".*?">','',html)
    texts=re.findall(res,page1,re.S|re.M)
    for m in texts:
        print(m)
   

#url='https://zsb.suda.edu.cn/view_markhistory.aspx?aa=2019年北京各专业录取分数一览表%A8&aid=1&ay=2019'
#print(getHTMLText(url))
#html=getHTMLText(url)
#parse_one_page(html)
#print(parse_one_page(html))
def parse_one_page1(html):

    res='<font.*?>(.*?)<.*?/font>'
    page1=re.sub('<a.*?=".*?">','',html)
    texts=re.findall(res,page1,re.S|re.M)
    return texts


def main(x,y,z):
    url='https://zsb.suda.edu.cn/view_markhistory.aspx?aa='+str(y)+'年'+str(z)+'各专业录取分数一览表&aid='+str(x)+'&ay='+str(y)
    html=getHTMLText(url)
    totaltext=parse_one_page1(html)
    return totaltext
province=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
alist=[]
for i in range(1,32):
    for j in range(2017,2020):
        t=[word.strip() for word in main(i,j,province[i-1])]
        alist.append(t)
    
print(alist)   
    
def Save_list(list1,filename):
    file2 = open(filename + '.txt', 'w')
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if j>1:
                if j%7==1:
                    file2.write('\n')
                    file2.write('')
                    file2.write('\t')
            file2.write(str(list1[i][j]))              # write函数不能写int类型的参数，所以使用str()转化
            file2.write('\t')                          # 相当于Tab一下，换一个单元格
        file2.write('\n')                              # 写完一行立马换行
    file2.close()
f=open('ceshi3.txt',mode='w')
Save_list(alist,'ceshi3.txt')

print(len(alist))
print(len(alist[0]))    
    