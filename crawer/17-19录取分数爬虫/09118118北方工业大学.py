import requests
import bs4
from bs4 import BeautifulSoup
import csv
#-*- coding:UTF-8 -*-
# get请求
def getHTMLText(url):
    response = requests.get(url) 
    response.encoding = 'utf-8' #查看原网页编码类型后设置对应的编码类型
    return response.text   #存储解码后的返回数据

#信息提取
def dataExtraction(rowData):
    plist=[] #存取录取信息
    soup = BeautifulSoup(rowData, "html.parser")
    
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds=tr.find_all('td')
            if(len(tds)==5):#是否为主表内容
                plist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
    
    return plist

#信息存储
def Datasave(year,plist,f_csv):
    for message in plist:
        if message[4]!= None and message[4]!='\xa0':
            f_csv.writerow(['北方工业大学',year,message[0],'文科','all',message[4],'09118118庄祎'])
        if message[3]!= None and message[3]!='\xa0':
            f_csv.writerow(['北方工业大学',year,message[0],'理科','all',message[3],'09118118庄祎'])

url_2019='http://bkzs.ncut.edu.cn/info/1072/2301.htm'
url_2018='http://bkzs.ncut.edu.cn/info/1072/2041.htm'
url_2017='http://bkzs.ncut.edu.cn/info/1072/1691.htm'

rowData_2019=getHTMLText(url_2019)
rowData_2018=getHTMLText(url_2018)
rowData_2017=getHTMLText(url_2017)

plist_2019=dataExtraction(rowData_2019)
plist_2018=dataExtraction(rowData_2018)
plist_2017=dataExtraction(rowData_2017)

with open('09118118庄祎-北方工业大学.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['College','Year','Province','Category','Major','Score','Contributor'])
    Datasave(2019,plist_2019,f_csv)
    Datasave(2018,plist_2018,f_csv)
    Datasave(2017,plist_2017,f_csv)