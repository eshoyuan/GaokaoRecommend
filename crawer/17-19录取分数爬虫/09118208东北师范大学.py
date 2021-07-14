# -*-  coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import openpyxl

def GetData(soup):
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

def tran(list):
    for u in list:
        if len(u)==3:
            temp=u[2]
            u[2]=u[1]
            u.append(temp)
    return list

def  wspy(url):
    rep=requests.get(url=url)
    rep.raise_for_status()
    rep.encoding='utf-8'
    html=rep.text
    soup=BeautifulSoup(html,"html.parser")
    infor=GetData(soup)
    return tran(infor)

allweb=[
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%8C%97%E4%BA%AC&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=f',   
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%A4%A9%E6%B4%A5&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B2%B3%E5%8C%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%B1%B1%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%86%85%E8%92%99%E5%8F%A4&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%B1%89%E6%8E%88%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E8%BE%BD%E5%AE%81&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%90%89%E6%9E%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E9%BB%91%E9%BE%99%E6%B1%9F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B1%9F%E8%8B%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%AE%89%E5%BE%BD&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E7%A6%8F%E5%BB%BA&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B1%9F%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%B1%B1%E4%B8%9C&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B2%B3%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B9%96%E5%8C%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B9%96%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',    
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%B9%BF%E4%B8%9C&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%B9%BF%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%B5%B7%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E9%87%8D%E5%BA%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%9B%9B%E5%B7%9D&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E8%B4%B5%E5%B7%9E&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E4%BA%91%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E8%A5%BF%E8%97%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E9%99%95%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E7%94%98%E8%82%83&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E9%9D%92%E6%B5%B7&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E5%AE%81%E5%A4%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2019&sf=%E6%96%B0%E7%96%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px='

'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%8C%97%E4%BA%AC&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',   
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%A4%A9%E6%B4%A5&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B2%B3%E5%8C%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%B1%B1%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%86%85%E8%92%99%E5%8F%A4&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%B1%89%E6%8E%88%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E8%BE%BD%E5%AE%81&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%90%89%E6%9E%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E9%BB%91%E9%BE%99%E6%B1%9F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B1%9F%E8%8B%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%AE%89%E5%BE%BD&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E7%A6%8F%E5%BB%BA&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B1%9F%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%B1%B1%E4%B8%9C&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B2%B3%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B9%96%E5%8C%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B9%96%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',    
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%B9%BF%E4%B8%9C&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%B9%BF%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%B5%B7%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E9%87%8D%E5%BA%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%9B%9B%E5%B7%9D&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E8%B4%B5%E5%B7%9E&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E4%BA%91%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E8%A5%BF%E8%97%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E9%99%95%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E7%94%98%E8%82%83&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E9%9D%92%E6%B5%B7&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E5%AE%81%E5%A4%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2018&sf=%E6%96%B0%E7%96%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px='

'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%8C%97%E4%BA%AC&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',   
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%A4%A9%E6%B4%A5&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B2%B3%E5%8C%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%B1%B1%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%86%85%E8%92%99%E5%8F%A4&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%B1%89%E6%8E%88%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E8%BE%BD%E5%AE%81&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%90%89%E6%9E%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E9%BB%91%E9%BE%99%E6%B1%9F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B1%9F%E8%8B%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%AE%89%E5%BE%BD&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E7%A6%8F%E5%BB%BA&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B1%9F%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%B1%B1%E4%B8%9C&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B2%B3%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B9%96%E5%8C%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B9%96%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',    
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%B9%BF%E4%B8%9C&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%B9%BF%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%B5%B7%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E9%87%8D%E5%BA%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%9B%9B%E5%B7%9D&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E8%B4%B5%E5%B7%9E&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E4%BA%91%E5%8D%97&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E8%A5%BF%E8%97%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E9%99%95%E8%A5%BF&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E7%94%98%E8%82%83&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E9%9D%92%E6%B5%B7&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%AE%81%E5%A4%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%96%B0%E7%96%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E5%AE%81%E5%A4%8F&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=',
'http://bkzsw.nenu.edu.cn/column.html?a=000018&b=000170&Action=Fraction&year=2017&sf=%E6%96%B0%E7%96%86&jhlb=%E4%B8%80%E8%88%AC%E8%AE%A1%E5%88%92&zylb=%E6%96%87%E5%8F%B2%E7%90%86%E5%B7%A5%E7%B1%BB&kelei=%E6%96%87%E7%A7%91&px=']

wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='College'
sheet['B1']='Year'
sheet['C1']='Province'
sheet['D1']='Category'
sheet['E1']='Major'
sheet['F1']='Score'
sheet['G1']='Contributor'
year=['2019','2018','2017']
province=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','江苏',
       '安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南',
       '重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
Score=['545','573','614','572','601','613','581','549','365','600',
       '593','589','568','573','583','595','577','556','741','587',
       '584','601','615','491','589','574','536','591','547']
contributor='09118208唐伟'
college='东北师范大学'
major='all'
sheet.title='东北师范大学高考录取分数线'

data_excel=[]
ynum=0
snum=0
wnum=0
while ynum<3:
    while snum<29:
        list=wspy(allweb[wnum])
        for u in list[1:]:                        
            data_excel.append([college,year[ynum],province[snum],
                               major,u[0],Score[snum],contributor])
        wnum=wnum+1
        snum=snum+1
    snum=0
    ynum=ynum+1
    

    
for item in data_excel:
    sheet.append(item)
wb.save('09118208唐伟-东北师范大学.csv')