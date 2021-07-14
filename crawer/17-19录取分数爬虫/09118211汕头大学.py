import requests
from bs4 import BeautifulSoup
import csv
from urllib import parse

def get(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    return html
list1=['2017年','2018年']
list2=['安徽','福建','广东','广西','河南','湖北','湖南','江苏','江西','山西','山东','四川','浙江']
list3=['理工','文史']
l1=[]
l2=[]
l3=[]
# 编码
for i in list1:
    l1.append(parse.quote(i))
for i in list2:
    l2.append(parse.quote(i))
for i in list3:
    l3.append(parse.quote(i))
urls=[]
for i in l1:
    for j in l2:
        for k in l3:
            urls.append('https://zs.stu.edu.cn/LQFS.aspx?year='+i+'&province='+j+'&subject='+k)
htmls=[]
for i in urls:
    htmls.append(get(i))
all=[]
y=[]
for i in htmls:
    soup = BeautifulSoup(i, 'html.parser')
    t = soup.find('div', {'id': 'ul_imgList', 'class': 'table-box'}).find_all('tr')
    for j in t:
        x=j.find_all('td')
        for k in x:
            y.append(k.get_text())
        all.append(y)
        y=[]
d=['年份', '省份', '科类', '批次', '专业名称', '录取人数', '平均分', '最高分', '最低分', '备注']
while d in all:
    all.remove(d)
l=[]
mycsv=[]
for i in all:
    l.append(i[0])
    l.append(i[1])
    l.append(i[2])
    l.append(i[4])
    l.append(i[8])
    mycsv.append(l)
    l=[]
with open("09118211黄花程-汕头大学.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(mycsv)
