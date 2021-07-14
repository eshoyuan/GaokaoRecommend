import requests
import string
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
#爬取南京工业大学的录取分数

#数据爬取函数
def reptile():
    sum=[]#用来存放初始爬取的数据
    r = requests.get('http://zhaosheng.njtech.edu.cn/newstudent/storeline')
    html = r.content
    soup=BeautifulSoup(html,'html.parser')
    score=soup.find_all('tr',attrs={'class':'tb_info_all_content'})
    for trtag in score:
        tdlist = trtag.find_all('td')
        init=[]#每一行的数据
        for i in range(0,7):
            init.append(tdlist[i].string)
        sum.append(init)

    for i in (range(2, 11)):#网址按数字排序，只要近三年的数据，网页上只需前10页的内容
        rr = requests.get('http://zhaosheng.njtech.edu.cn/newstudent/storeline?page=' + str(i))
        htmli = rr.content
        soupi = BeautifulSoup(htmli, 'html.parser')
        ss=soupi.find_all('tr',attrs={'class':'tb_info_all_content'})#获取表格中每一行的标签
        for trtag in ss:
            tdlist = trtag.find_all('td')#每一个数据的标签
            init = []
            for i in range(0, 7):#每一行数据固定为7个
                init.append(tdlist[i].string)#将bs4的tag类型转换为string
            sum.append(init)
    return sum

#数据格式清洗函数
def clear(sum):
    #sum=reptile()
    scoretable=[]
    for i in range(0,len(sum)):
        if sum[i][0] in ['2019','2018','2017'] and sum[i][3] in ['本科普通批','本科','1','普通批','1A','本科A阶段','1B','普通类','本科A批','普通类本科批','1I普通类']:
            scoretable.append(sum[i])#确认年份要求
                                     #确认批次(去除非本科批后，没有艺术等科类，所以不用再对科类做筛选)
    for i in scoretable:#删除多余列
        del i[3] #删除后列索引发生动态变化，删除345列要写删除333列
        del i[3]
        del i[3]
    for i in scoretable:#插入时索引变化同删除一样
        i.insert(0,'南京工业大学')
        i.insert(4,'all')#无专业分，统一为all
        i.insert(6,'09118145邵彤')
    return scoretable




sum=reptile()
sum=clear(sum)
#表明表格的表头
tablename=['College','Year','Province','Category','Major','Score','Contributor']
table=pd.DataFrame(columns=tablename,data=sum)
#写入csv
table.to_csv('D:/09118145邵彤-南京工业大学.csv',index=False,encoding="UTF-8")








