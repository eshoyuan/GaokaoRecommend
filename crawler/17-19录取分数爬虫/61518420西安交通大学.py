# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:24:59 2020

@author: yao
"""

from bs4 import BeautifulSoup
import requests
import csv


useless_major=["理工","文史"] #确定不需要的专业名
'''###################爬取网站上可查找的年份和省市##################'''
url = "http://zs.xjtu.edu.cn/bkscx/lnlqcx.htm" #西安交通大学本科招生网历年录取分数查询网址
response = requests.get(url)#发送get请求
response.encoding = 'UTF-8'
soup = BeautifulSoup(response.text, 'lxml')
soup=soup.select("option")
parameter_list=[]
for i in soup:
    parameter_list.append(i.get_text())
#可查询的年份（注：原网站上有2016年分数线的选项，但是其中无2016年录取分数线的数据，因此csv文件中无2016年录取分数线信息）
year=parameter_list[0:4]
province=parameter_list[5:]#可查询的省市
'''#########################创建文件对象#################################'''
# 1. 创建文件对象
f = open('西安交通大学录取分数线.csv','w',encoding='utf-8-sig',newline='')
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)
# 3. 构建列表头
csv_writer.writerow(["College","Year","Province","Category","Major","Score","Contributer"])
'''############################爬取录取分数线###############################'''
for year_i in year:#年份
    for province_j in province:#省市
        print("开始爬取",year_i,"年",province_j,"录取分数线")
        url = "http://zs.xjtu.edu.cn/lnlqjg.jsp?wbtreeid=1167"#西安交通大学本科招生网历年录取分数查询网址
        params={"nf":year_i,"sf":province_j}#观察得出form表单所需的参数字典
        response = requests.post(url,params)#发送提交表单请求
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'lxml')
        soup=soup.select("td",id="fybt")#选取所需数据
        result=[]#最终结果写入列表
        for i in soup:
            result.append(i.get_text())
        index_start=result.index(" 最低分 ")#丢弃列表开始时的冗余信息
        result=result[index_start+1:]
        for i in result:#删除不需要的专业分数
            for j in useless_major:
                if i==j:
                    t=result.index(i)
                    del result[t:t+4]
        for i in range(0,int(len(result)/4)):#分行写入csv文件
            temp=result[4*i:4*i+4]
            temp=temp[0:4:3]
            list_head=["西安交通大学",year_i,province_j," "]#表头信息
            list_tail=["61518420姚杳"]#表尾信息
            temp=list_head+temp+list_tail
            csv_writer.writerow(temp)#写入csv文件
        print(year_i,"年",province_j,"录取分数线爬取完毕")
'''######################################################################'''   
print("西安交通大学录取分数线爬取完毕！")
