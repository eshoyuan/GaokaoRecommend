"""
author:Haotian Li   Date:2020/5/13 20h
一开始分配的学校是'中国农业大学'，但在获取ajax的json文件时频繁出现403错误；
并不是代码问题，因为我用同样的代码获得了类似网页结构的'南京大学'的数据；
之后老师给的'北京联合大学'，该学校只在部分省份为一本，为满足需求中的'本一批次'，
只爬取了该部分省份的录取分数，因为数据较少又额外爬取了16年的数据。
"""

from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import re


def getandWrite(url):
    allItem=[]  # 存放爬取的所有信息
    usefulItem=[]  # 存放爬取的有用信息
    page = urllib.request.urlopen(url)
    bs = BeautifulSoup(page,'html.parser')
    year = bs.title.get_text()[0:4]  # 获取对应年份

    # 提取文本信息
    for item in bs.find_all("td"):
        allItem.append(item.get_text())

    # 该校在2016年在11个省份中为本一批次，之后三年为10个省份，
    # 且静态网页数据格式很不同，需要单独处理。
    if year =='2016':
        for i in range(11):
            Witem = ['北京联合大学', year, re.sub("[\r\t\n]","",allItem[11+i * 9]), '文科', 'all',
                     re.sub("[\r\t\n]","",allItem[i * 9 + 15]), '09118111李浩天']
            Litem = ['北京联合大学', year, re.sub("[\r\t\n]","",allItem[11+i * 9]), '理科', 'all',
                     re.sub("[\r\t\n]","",allItem[i * 9 + 18]), '09118111李浩天']
            usefulItem.append(Witem)
            usefulItem.append(Litem)
    else:
        for i in range(1,11):
            Witem = ['北京联合大学', year, allItem[i*9].replace("\n",""), '文科', 'all',
                     allItem[i*9+4].replace("\n",""), '09118111李浩天']
            Litem = ['北京联合大学', year, allItem[i*9].replace("\n",""), '理科', 'all',
                     allItem[i*9+7].replace("\n",""), '09118111李浩天']
            usefulItem.append(Witem)
            usefulItem.append(Litem)

    return usefulItem


if __name__ == '__main__':
    url2019 = "https://zsxx.buu.edu.cn/news/show-681.html"
    url2018 = "https://zsxx.buu.edu.cn/news/show-501.html"
    url2017 = "https://zsxx.buu.edu.cn/news/show-378.html"
    url2016 = "https://zsxx.buu.edu.cn/news/show-230.html"
    result2019 = getandWrite(url2019)
    result2018 = getandWrite(url2018)
    result2017 = getandWrite(url2017)
    result2016 = getandWrite(url2016)

    # 写入csv
    with open('./09118111李浩天-北京联合大学.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['College','Year','Province','Category','Major','Score','Contributer'])
        for row in result2019:
            writer.writerow(row)
        for row in result2018:
            writer.writerow(row)
        for row in result2017:
            writer.writerow(row)
        for row in result2016:
            writer.writerow(row)