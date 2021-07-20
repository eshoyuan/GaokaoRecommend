# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:00:27 2020

@author: 我会学习的
"""

import requests        #导入requests包
import json
import csv
import codecs
# codecs 是自然语言编码转换模块
ssmc=["北京","天津","河北","山西","内蒙","辽宁","吉林","黑龙江",
      "上海","江苏","浙江","安徽","福建","江西","山东","河南",
      "湖北","湖南","广东","广西","海南","重庆"
      ,"四川","贵州","云南","西藏","陕西","甘肃","宁夏","新疆"]
klmc=["理工","文史"]
nf=["2019","2018","2017"]
alldata=[]
for a in ssmc:
    for b in klmc:
        for c in nf:
            url = 'http://www.goto.buct.edu.cn/f/cjcxxianshi'
            data1={"ssmc":a,"klmc":b,"nf":c}
            headers1={"Host": "www.goto.buct.edu.cn",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
                      "Accept": "application/json, text/javascript, */*; q=0.01",
                      "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                      "Accept-Encoding": "gzip, deflate",
                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                      "X-Requested-With": "XMLHttpRequest",
                      "Content-Length": "55",
                      "Origin": "http://www.goto.buct.edu.cn",
                      "Connection": "keep-alive",
                      "Referer": "http://www.goto.buct.edu.cn/f/cjcx",
                      "Cookie": "jeesite.session.id=cf4c9ee30fa945ef9c33ec04ff11ef5d"}
            r = requests.post(url,data=data1,headers=headers1)        
            r.encoding='utf-8'
            texts=json.loads(r.text)
            indexes=["nf","ssmc","klmc","zymc","minScore"]
            for i in texts:
                onedata=[]
                onedata.append("北京化工大学")
                for key in indexes:
                    onedata.append(i[key])
                onedata.append("09118109曾家俊")
                alldata.append(onedata)   
#print(len(alldata))


fileName = 'entry_score.csv'

# 指定编码为 utf-8, 避免写 csv 文件出现中文乱码
with codecs.open(fileName, 'w', 'gbk') as csvfile:
# 指定 csv 文件的头部显示项
    filednames = ['College', 'Year','Province','Categpry','Major','Score','Contributor']
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for item in alldata:
        try:
            writer.writerow({'College':item[0], 'Year':item[1],'Province':item[2],'Categpry':item[3],'Major':item[4],'Score':item[5],'Contributor':item[6]})
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")