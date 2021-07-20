# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:43:34 2020

@author: Administrator
"""
#引入相关库
import csv
import urllib.parse  
import urllib.request

def getProvYearText (url,prov,year):
    '''
    调取某省份某年录取分数信息文本信息列表
    '''
    #防止异常读取
    try:
        values={'province':prov,'year':year}
        data=urllib.parse.urlencode(values).encode("utf-8")
        #创建请求对象  
        req=urllib.request.Request(url,data)
        #获得服务器返回的数据  
        response=urllib.request.urlopen(req) 
        #处理数据  
        page=response.read().decode("utf-8")
        page_split = page.split(",")
        return page_split
    except:
        return ""

#设置有关参数
url='http://zhaosheng.hdu.edu.cn/deal.php'
prov_list = ['浙江省','安徽省','北京市','福建省','甘肃省','港澳台',
             '广东省','广西区','贵州省','海南省','河南省','河北省',
             '黑龙江省','湖北省','湖南省','江苏省','江西省','辽宁省',
             '内蒙古区','宁夏区','青海省','山东省','山西省','陕西省',
             '上海市','四川省','西藏区','新疆区','云南省','重庆市','天津市']
prov_name = ['浙江','安徽','北京','福建','甘肃','港澳台',                   #规范名称
             '广东','广西','贵州','海南','河南','河北',
             '黑龙江','湖北','湖南','江苏','江西','辽宁',
             '内蒙古','宁夏','青海','山东','山西','陕西',
             '上海','四川','西藏','新疆','云南','重庆','天津']
year_list = ['2019','2018','2017','2016']


#写入文件
with open('61518422石知一-杭州电子科技大学.csv','w',newline='',)  as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])
    for year in year_list:
        for j in range(len(prov_list)):
                r = getProvYearText(url,prov_list[j],year)#获取某一年某一省份录取分数线
                for i in range(int(len(r)/7)):
                    cate = r[i*7]
                    cate = cate.lstrip()
                    cate = cate.rstrip()
                    if(cate=='理工类' or cate=='理科'):#统一格式
                        cate = '理科'
                    elif(cate=='文史类' or cate=='文科'):
                        cate = '文科'
                    elif(cate=='不分文理'):
                        cate = 'all'
                    else:
                        continue
                    major = r[i*7+2]
                    major = major.lstrip()
                    major = major.rstrip()
                    score = r[i*7+5]
                    csv_writer.writerow(["杭州电子科技大学",year,prov_name[j],cate,major,score,'61518422石知一'])














