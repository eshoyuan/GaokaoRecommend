# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:35:12 2020

@author: Ted Fang
"""

from bs4 import BeautifulSoup
import re
import urllib
import random
import bs4
import csv
#青岛大学的历年录取分数信息为静态网页，且只给出了19年的具体专业分数，18，17年仅给出了当年文理科的录取分数

def askurl(url):#记录此网页的完整信息
    request = urllib.request.Request(url,headers={'User-Agent': random.choice(header)})#随机获取伪装头
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#由于该学校静态网页并不规范，不同省份的录取分数页面表格的构造并不同，其中，湖南浙江海南和青海的录取分数表格与众不同，需单独编写，
    #另外，西藏的录取形式与众不同，山东的表格不明确，本次不予编写
    #由于以下函数使用方法基本相同，仅详细注释getData_others函数
def getData_Hunan():   
        datalist_Hunan= []    
        c_url = 'https://zs.qdu.edu.cn/info/1026/1091.htm'
        html = askurl(c_url)
        soup = BeautifulSoup(html,"html.parser")        
        c_information_17_18 = re.findall(re.compile(r'font-size: 16px;">(\d*)</span></p></td>'),str(soup))
        datalist_Hunan.append(['2017','湖南','理科','all',c_information_17_18[10]])#取出17，18年的湖南录取数据
        datalist_Hunan.append(['2017','湖南','文科','all',c_information_17_18[1]])
        datalist_Hunan.append(['2018','湖南','理科','all',c_information_17_18[13]])
        datalist_Hunan.append(['2018','湖南','文科','all',c_information_17_18[4]])
        #19年有具体专业的数据，接下来开始取出19年的数据
        for tr in soup.find_all('tbody')[1].children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')            
                c_major = re.findall(re.compile(r'valign="middle" width="72">(.*?)</td>'),str(tds[0]))
                c_catagory = re.findall(re.compile(r'<td align="center" valign="middle" width="52">(.)</td>'),str(tds[1]))
                c_score = re.findall(re.compile(r'>(\d*)</td>'),str(tds[4]))                
                if c_score != [] and c_catagory != [] and c_major != []:
                    datalist_Hunan.append(['2019','湖南',c_catagory[0],c_major[0],c_score[0]])
        #print(datalist_Hunan)
        return datalist_Hunan#返回一个列表，记录着湖南省的录取信息

def getData_Zhejiang():   
        datalist_Zhejiang= []    
        c_url = 'https://zs.qdu.edu.cn/info/1026/1005.htm'
        html = askurl(c_url)
        soup = BeautifulSoup(html,"html.parser")        
        c_information_17_18 = re.findall(re.compile(r'color:black">(.*?)</span></p></td>'),str(soup))
        #print(c_information_17_18)
        datalist_Zhejiang.append(['2017','浙江',' ',' ',c_information_17_18[2]])#取出17，18年的浙江录取数据
        datalist_Zhejiang.append(['2018','浙江',' ',' ',c_information_17_18[5]])
        #19年有具体专业的数据，接下来开始取出19年的数据
        for tr in soup.find_all('tbody')[1].children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                #print(tds[0])
                c_major = re.findall(re.compile(r'valign="middle" width="87">(.*?)</td>'),str(tds[0]))
                c_score = re.findall(re.compile(r'>(\d*)</td>'),str(tds[3]))                
                if c_score == [] or c_major == []:
                   continue
                else:
                   datalist_Zhejiang.append(['2019','浙江',' ',c_major[0],c_score[0]])
        #print(datalist_Zhejiang)
        return datalist_Zhejiang #返回一个列表，记录着浙江省的录取信息        
       
def getData_others(baseurl):
    datalist= []
    for i in range(len(province)):#采用循环进入不同省份对应的链接
        c_url= 'https://zs.qdu.edu.cn/info/1026/' +str(province[i])+'.htm'
        html = askurl(c_url)
        soup = BeautifulSoup(html,"lxml")
        c_province = re.findall(re.compile(r'<h3 align="center" class="details-title text-center">(.*?)</h3>'),str(soup.find('h3')))#找出当前网页对应的省份                
        c_major =[]
        c_catagory=[]
        c_score=[]
        for tr in soup.find_all('tbody')[1].children:#使用提取标签的方法提取出网页上第二个表格的数据，即19年的数据
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                tds[0].string=tds[0].string.replace(u'\xa0',u'')#防止最后读取的数据中含有\xa0，将其提前替换防止写入csv表格时报错
                tds[1].string=tds[1].string.replace(u'\xa0',u'')
                tds[3].string=tds[3].string.replace(u'\xa0',u'')
                c_major.append(tds[0].string)
                #print(tds[3].string)
                c_catagory.append(tds[1].string)
                c_score.append(tds[3].string)
        c_catagory.pop(0)#提取的第一项不是数据而是表头，因此舍去
        c_major.pop(0)
        c_score.pop(0)
        for i in range(len(c_score)):
            datalist.append(['2019',c_province[0],c_catagory[i],c_major[i],c_score[i]])
        c_information_17_18=[]
        for tr in soup.find_all('tbody')[0].children:#提取网页中第一个表格的信息，其中包含17和18年的数据信息
            if isinstance(tr,bs4.element.Tag):
                tds_ = tr('td')
                for td in tds_:
                    #print(td.string)
                    c_information_17_18.append(td.string)
        datalist.append(['2017',c_province[0],'理科','all',c_information_17_18[29]])
        datalist.append(['2017',c_province[0],'文科','all',c_information_17_18[19]])
        datalist.append(['2018',c_province[0],'理科','all',c_information_17_18[32]])
        datalist.append(['2018',c_province[0],'文科', 'all',c_information_17_18[22]])
        #print(datalist)
    return(datalist)
                   
def getData_Hainan():
    datalist_Hainan= []    
    c_url= 'https://zs.qdu.edu.cn/info/1026/1096.htm'
    html = askurl(c_url)
    soup = BeautifulSoup(html,"lxml")
    c_province = re.findall(re.compile(r'<h3 align="center" class="details-title text-center">(.*?)</h3>'),str(soup.find('h3')))#找出当前网页对应的省份                
    c_major =[]
    c_catagory=[]
    c_score=[]
    information19=[]
    for tr in soup.find_all('tbody')[1].children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')  
            for td in tds:
                information19.append(td.string)
    for i in range(0,15):        
        c_major.append(information19[7*i+8])
        c_catagory.append(information19[7*i+9])
        c_score.append(information19[7*i+11])
    for i in range(len(c_score)):
        datalist_Hainan.append(['2019',c_province[0],c_catagory[i],c_major[i],c_score[i]])
    c_information_17_18=[]
    for tr in soup.find_all('tbody')[0].children:
        if isinstance(tr,bs4.element.Tag):
            tds_ = tr('td')
            for td in tds_:
                c_information_17_18.append(td.string)
    datalist_Hainan.append(['2017',c_province[0],'理科','all',c_information_17_18[31]])
    datalist_Hainan.append(['2017',c_province[0],'文科','all',c_information_17_18[20]])
    datalist_Hainan.append(['2018',c_province[0],'文科','all',c_information_17_18[24]])
    datalist_Hainan.append(['2018',c_province[0],'理科', 'all',c_information_17_18[34]])
    #print(c_information_17_18)
    #print(datalist_Hainan)
    return(datalist_Hainan)        
              
def getData_Qinghai():
    datalist_Qinghai= []    
    c_url= 'https://zs.qdu.edu.cn/info/1026/1084.htm'
    html = askurl(c_url)
    soup = BeautifulSoup(html,"lxml")
    c_province = re.findall(re.compile(r'<h3 align="center" class="details-title text-center">(.*?)</h3>'),str(soup.find('h3')))#找出当前网页对应的省份                
    c_major =[]
    c_catagory=[]
    c_score=[]
    information19=[]
    for tr in soup.find_all('tbody')[1].children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')  
            for td in tds:
                #print(td.string)
                information19.append(td.string)
    for i in range(0,14):        
        c_major.append(information19[6*i+6])
        c_catagory.append(information19[6*i+7])
        c_score.append(information19[6*i+9])
    for i in range(len(c_score)):
        datalist_Qinghai.append(['2019',c_province[0],c_catagory[i],c_major[i],c_score[i]])
    c_information_17_18=[]
    for tr in soup.find_all('tbody')[0].children:
        if isinstance(tr,bs4.element.Tag):
            tds_ = tr('td')
            for td in tds_:
                c_information_17_18.append(td.string)
    datalist_Qinghai.append(['2017',c_province[0],'理科','all',c_information_17_18[29]])
    datalist_Qinghai.append(['2017',c_province[0],'文科','all',c_information_17_18[19]])
    datalist_Qinghai.append(['2018',c_province[0],'理科','all',c_information_17_18[32]])
    datalist_Qinghai.append(['2018',c_province[0],'文科', 'all',c_information_17_18[22]])
    #print(datalist_Qinghai)
    return(datalist_Qinghai) 
        
url ='https://zs.qdu.edu.cn/index/lnfs.htm'
header= [# 谷歌
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.html.2171.71 Safari/537.36',
        'Mozilla/5.0.html (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.html.1271.64 Safari/537.11',
        'Mozilla/5.0.html (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.html.648.133 Safari/534.16',
        # 火狐
        'Mozilla/5.0.html (Windows NT 6.1; WOW64; rv:34.0.html) Gecko/20100101 Firefox/34.0.html',
        'Mozilla/5.0.html (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        # opera
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.html.2171.95 Safari/537.36 OPR/26.0.html.1656.60',
        # qq浏览器
        'Mozilla/5.0.html (compatible; MSIE 9.0.html; Windows NT 6.1; WOW64; Trident/5.0.html; SLCC2; .NET CLR 2.0.html.50727; .NET CLR 3.5.30729; .NET CLR 3.0.html.30729; Media Center PC 6.0.html; .NET4.0C; .NET4.0E; QQBrowser/7.0.html.3698.400)',
        # 搜狗浏览器
        'Mozilla/5.0.html (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.html.963.84 Safari/535.11 SE 2.X MetaSr 1.0.html',
        # 360浏览器
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.html.1599.101 Safari/537.36',
        'Mozilla/5.0.html (Windows NT 6.1; WOW64; Trident/7.0.html; rv:11.0.html) like Gecko',
        # uc浏览器
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.html.2125.122 UBrowser/4.0.html.3214.0.html Safari/537.36']
province = [1104,1088,1092,1097,1098,1085,1100,1102,1093,1010,
             1086,1087,1101,1083,1009,1008,1094,1090,1011,1006,1089,1099,1095,1103]       
getData_Hunan()
getData_Zhejiang()
getData_others(url)
getData_Hainan()
getData_Qinghai()
datalist_all=getData_Hunan()+getData_Zhejiang()+getData_others(url)+getData_Hainan()+getData_Qinghai()
with open( '61518315方大政-青岛大学.csv', 'w',newline='' ,) as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['College' ,'Year' ,'Province' ,'Category' , 'Major' ,'Score', 'Contributor'])  
    for i in range(len(datalist_all)):
        csv_writer.writerow( ["青岛大学" ,datalist_all[i][0],datalist_all[i][1], datalist_all[i][2],datalist_all[i][3],datalist_all[i][4], '61518315方大政'])




































