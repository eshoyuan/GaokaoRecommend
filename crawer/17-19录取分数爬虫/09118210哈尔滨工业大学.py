import requests
from bs4 import BeautifulSoup

import openpyxl

def take(soup):
    list=[]
    data=soup.find_all('tr')
    for tr in data:
        ltd=tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv=[]
        for td in ltd:
            singleUniv.append(td.string)
        list.append(singleUniv)
    return list
def make(list):
    for u in list:
        if len(u)==3:
            temp=u[2]
            u[2]=u[1]
            u.append(temp)
    return list
def  mk(target):
    rep=requests.get(url=target)
    rep.raise_for_status()
    rep.encoding='UTF-8'
    html1=rep.text
    soup=BeautifulSoup(html1,"html.parser")
    inf=take(soup)
    return make(inf)
tt=['https://zsb.hit.edu.cn/information/score?province=北京&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%A4%A9%E6%B4%A5&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B2%B3%E5%8C%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%B1%B1%E8%A5%BF&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%86%85%E8%92%99%E5%8F%A4&year=2019','https://zsb.hit.edu.cn/information/score?province=%E8%BE%BD%E5%AE%81&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%90%89%E6%9E%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E9%BB%91%E9%BE%99%E6%B1%9F&year=2019','https://zsb.hit.edu.cn/information/score?province=%E4%B8%8A%E6%B5%B7&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B1%9F%E8%8B%8F&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B5%99%E6%B1%9F&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%AE%89%E5%BE%BD&year=2019','https://zsb.hit.edu.cn/information/score?province=%E7%A6%8F%E5%BB%BA&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B1%9F%E8%A5%BF&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%B1%B1%E4%B8%9C&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B2%B3%E5%8D%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B9%96%E5%8C%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B9%96%E5%8D%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%B9%BF%E4%B8%9C&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%B9%BF%E8%A5%BF&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%B5%B7%E5%8D%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E9%87%8D%E5%BA%86&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%9B%9B%E5%B7%9D&year=2019','https://zsb.hit.edu.cn/information/score?province=%E8%B4%B5%E5%B7%9E&year=2019','https://zsb.hit.edu.cn/information/score?province=%E4%BA%91%E5%8D%97&year=2019','https://zsb.hit.edu.cn/information/score?province=%E8%A5%BF%E8%97%8F&year=2019','https://zsb.hit.edu.cn/information/score?province=%E9%99%95%E8%A5%BF&year=2019','https://zsb.hit.edu.cn/information/score?province=%E7%94%98%E8%82%83&year=2019','https://zsb.hit.edu.cn/information/score?province=%E9%9D%92%E6%B5%B7&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%AE%81%E5%A4%8F&year=2019','https://zsb.hit.edu.cn/information/score?province=%E6%96%B0%E7%96%86&year=2019','https://zsb.hit.edu.cn/information/score?province=%E5%8C%97%E4%BA%AC&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%A4%A9%E6%B4%A5&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B2%B3%E5%8C%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%B1%B1%E8%A5%BF&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%86%85%E8%92%99%E5%8F%A4&year=2018','https://zsb.hit.edu.cn/information/score?province=%E8%BE%BD%E5%AE%81&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%90%89%E6%9E%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E9%BB%91%E9%BE%99%E6%B1%9F&year=2018','https://zsb.hit.edu.cn/information/score?province=%E4%B8%8A%E6%B5%B7&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B1%9F%E8%8B%8F&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B5%99%E6%B1%9F&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%AE%89%E5%BE%BD&year=2018','https://zsb.hit.edu.cn/information/score?province=%E7%A6%8F%E5%BB%BA&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B1%9F%E8%A5%BF&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%B1%B1%E4%B8%9C&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B2%B3%E5%8D%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B9%96%E5%8C%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B9%96%E5%8D%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%B9%BF%E4%B8%9C&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%B9%BF%E8%A5%BF&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%B5%B7%E5%8D%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E9%87%8D%E5%BA%86&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%9B%9B%E5%B7%9D&year=2018','https://zsb.hit.edu.cn/information/score?province=%E8%B4%B5%E5%B7%9E&year=2018','https://zsb.hit.edu.cn/information/score?province=%E4%BA%91%E5%8D%97&year=2018','https://zsb.hit.edu.cn/information/score?province=%E8%A5%BF%E8%97%8F&year=2018','https://zsb.hit.edu.cn/information/score?province=%E9%99%95%E8%A5%BF&year=2018','https://zsb.hit.edu.cn/information/score?province=%E7%94%98%E8%82%83&year=2018','https://zsb.hit.edu.cn/information/score?province=%E9%9D%92%E6%B5%B7&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%AE%81%E5%A4%8F&year=2018','https://zsb.hit.edu.cn/information/score?province=%E6%96%B0%E7%96%86&year=2018','https://zsb.hit.edu.cn/information/score?province=%E5%8C%97%E4%BA%AC&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%A4%A9%E6%B4%A5&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B2%B3%E5%8C%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%B1%B1%E8%A5%BF&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%86%85%E8%92%99%E5%8F%A4&year=2017','https://zsb.hit.edu.cn/information/score?province=%E8%BE%BD%E5%AE%81&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%90%89%E6%9E%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E9%BB%91%E9%BE%99%E6%B1%9F&year=2017','https://zsb.hit.edu.cn/information/score?province=%E4%B8%8A%E6%B5%B7&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B1%9F%E8%8B%8F&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B5%99%E6%B1%9F&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%AE%89%E5%BE%BD&year=2017','https://zsb.hit.edu.cn/information/score?province=%E7%A6%8F%E5%BB%BA&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B1%9F%E8%A5%BF&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%B1%B1%E4%B8%9C&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B2%B3%E5%8D%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B9%96%E5%8C%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B9%96%E5%8D%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%B9%BF%E4%B8%9C&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%B9%BF%E8%A5%BF&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%B5%B7%E5%8D%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E9%87%8D%E5%BA%86&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%9B%9B%E5%B7%9D&year=2017','https://zsb.hit.edu.cn/information/score?province=%E8%B4%B5%E5%B7%9E&year=2017','https://zsb.hit.edu.cn/information/score?province=%E4%BA%91%E5%8D%97&year=2017','https://zsb.hit.edu.cn/information/score?province=%E8%A5%BF%E8%97%8F&year=2017','https://zsb.hit.edu.cn/information/score?province=%E9%99%95%E8%A5%BF&year=2017','https://zsb.hit.edu.cn/information/score?province=%E7%94%98%E8%82%83&year=2017','https://zsb.hit.edu.cn/information/score?province=%E9%9D%92%E6%B5%B7&year=2017','https://zsb.hit.edu.cn/information/score?province=%E5%AE%81%E5%A4%8F&year=2017','https://zsb.hit.edu.cn/information/score?province=%E6%96%B0%E7%96%86&year=2017']

list1=mk(tt[0])

wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='Collega'
sheet['B1']='Year'
sheet['C1']='Province'
sheet['D1']='Category'
sheet['E1']='Major'
sheet['F1']='Score'
sheet['G1']='Contributor'

year=['2019','2018','2017']
name='哈尔滨工业大学'
place=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','河北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
contributor='09118210边浩文'
sheet.title='哈尔滨工业大学近三年录取分数线'
data_excel=[]

number1=0
number2=0
number3=0
while number1<3:
    while number2<31:
        list=mk(tt[number3])
        for u in list[1:]:
            
            
            data_excel.append([name,year[number1],place[number2],u[1],u[0],u[4],contributor])
        number3=number3+1
        number2=number2+1
    number2=0
    number1=number1+1

    
for each in data_excel:
    sheet.append(each)
wb.save('哈尔滨工业大学录取.csv')


















