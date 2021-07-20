import requests
import bs4
from bs4 import BeautifulSoup
import re
import csv

def getHTMLText(url):
    '''读取url上的文本信息'''

    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，则引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def otherProvinceList(otherList, html):
    '''将读取的其他省份的分数文本信息存成一个列表'''

    # 解析html代码
    soup = BeautifulSoup(html, "html.parser")

    # 获得tbody标签下所有存放有用信息的tr标签
    trs = []
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            trs.append(tr)
    trs = trs[6:]

    # 每一条tr标签生成3条不同年份的信息
    province = ''
    for tr in trs:
        tds = tr('td')  # 获得该tr标签下的所有td标签

        # 处理特殊的tr标签下td标签的索引
        j = 0
        for i in range(len(tds)):
            match = re.match(r'^理|^文|综', tds[i].string)
            if match:
                j = i
                break
        if j != 0:
            province = tds[j-1].string

        # 生成3条不同年份的信息
        year = "2019"
        otherList.append(["首都师范大学", year, province, tds[j].string, "all",
                      tds[j+1].string, "09118130武逸仙"])
        year = "2018"
        otherList.append(["首都师范大学", year, province, tds[j].string, "all",
                      tds[j+4].string, "09118130武逸仙"])
        year = "2017"
        otherList.append(["首都师范大学", year, province, tds[j].string, "all",
                      tds[j+7].string, "09118130武逸仙"])

def BeiJingList(BJList, html):
    '''将读取的北京的分数文本信息存成一个列表'''

    # 解析html代码
    soup = BeautifulSoup(html, "html.parser")

    # 获得tbody标签下所有存放有用信息的tr标签
    trs = []
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            trs.append(tr)
    trs = trs[2:]

    # 每一条tr标签生成3条不同年份的信息
    province = "北京"
    major = ''
    for tr in trs:
        tds = tr('td')  # 获得该tr标签下的所有td标签

        # 处理特殊的tr标签下td标签的索引
        j = 0
        for i in range(len(tds)):
            if tds[i].string == "理" or tds[i].string == "文":
                j = i
                break
        if j != 0:
            major = tds[j-1].string

        # 生成3条不同年份的信息
        year = "2019"
        BJList.append(["首都师范大学", year, province, tds[j].string, major,
                       tds[j + 1].string, "09118130武逸仙"])
        year = "2018"
        BJList.append(["首都师范大学", year, province, tds[j].string, major,
                       tds[j + 4].string, "09118130武逸仙"])
        year = "2017"
        BJList.append(["首都师范大学", year, province, tds[j].string, major,
                       tds[j + 7].string, "09118130武逸仙"])

def store_to_csv(totalList):
    '''将爬取的信息存为一个csv文件'''

    headers = ['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor']
    with open('09118130武逸仙-首都师范大学.csv','w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(totalList)


totalList = []  # 存放所有省份的分数信息
BJList = []  # 存放北京的分数信息

otherUrl = "http://bkzs.cnu.edu.cn/info/1019/1300.htm"
otherHtml = getHTMLText(otherUrl)  # 读取除北京外其他省份的分数文本信息
otherProvinceList(totalList, otherHtml)  # 将文本信息转换为一个列表储存

BJUrl = "http://bkzs.cnu.edu.cn/info/1019/1299.htm"
BJHtml = getHTMLText(BJUrl)  # 读取北京的分数文本信息
BeiJingList(BJList, BJHtml)  # 将文本信息转换为一个列表储存

totalList.extend(BJList)
store_to_csv(totalList)  # 将爬取的信息存为csv文件
print("爬取成功！")

