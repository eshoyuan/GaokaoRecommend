import requests        #导入requests包
import re
import csv
import time

cityids=[11,31,32,44,41,33,42,12,13,15,13,21,22,23,50,36,37,34,35,43,46,45,51,52,53,62,61,63,64,54,65]
# 城市id
years=[2019,2018,2017, 2016]
# 提取年份
rows = [['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor']]
#表头
for y in  years:
    print(y)
    for city in cityids:
        time.sleep(5)
        # 防止频繁访问被封ip
        print(city)
        url = 'https://zs.bsu.edu.cn/api/score/list?year='+str(y)+'&category=0&cityId='+str(city)+'&subject=-1'
        # print(url)
        strhtml = requests.get(url)
        # print(strhtml.text)
        result = re.sub(r'{|}', '', strhtml.text)
        result = re.sub(r'.*\[|]', '', result)
        result = re.sub(r'\"', '', result)
        result = re.split(r'id:\d+,', result)
        College = ['北京体育大学']
        Year = ['']
        Province = ['']
        Category = ['all']
        Major = ['']
        Score = ['']
        Contributer = ['胡艺凡']
        # 存储信息的list
        for i in result:#下面为数据筛选
            # print(i)
            if (i):
                City_result = re.split(r'cityName:', i)[1].split(r',')[0]
                Province[0] = City_result
                major = re.split(r'major:', i)[1].split(r',')[0]
                Major[0] = major
                category = re.split(r'subject:', i)[1].split(r',')[0]
                if (int(category) == 0):
                    Category[0] = '理科'
                elif(int(category) == 0):
                    Category[0] = '文科'
                #如果没有文理科之分则为all
                year = re.split(r'year:', i)[1].split(r',')[0]
                Year[0] = year
                score = re.split(r'culturalMinScore:', i)[1].split(r',')[0]
                Score[0] = score
                if score == '/' :
                    Score[0]='None'
                row = []
                row.append(College[0])
                row.append(Year[0])
                row.append(Province[0])
                row.append(Category[0])
                row.append(Major[0])
                row.append(Score[0])
                row.append(Contributer[0])
                rows.append(row)
out=open('09118127胡艺凡-北京体育大学.csv','w',newline='')
writer=csv.writer(out)
for i in rows:
    writer.writerow(i)
# url = 'https://zs.bsu.edu.cn/api/score/list?year=2019&category=0&cityId=12&subject=-1'
# strhtml = requests.get(url)        #Get方式获取网页数据
# # print(rows)
# # soup=BeautifulSoup(strhtml.text,'lxml')
# print(strhtml.text)
# print(type(strhtml.text))
# result= re.sub(r'{|}','',strhtml.text)
# result=re.sub(r'.*\[|]','',result)
# result=re.sub(r'\"','',result)
# print(result)
# City_result=re.split(r'cityName:',result)[1].split(r',')[0]
# # 获得城市地址
# result=re.split(r'id:\d+,',result)
# rows=[['College','Year','Province','Category','Major','Score','Contributor']]
# College=['北京体育大学']
# Year=['']
# Province=['']
# Category=['']
# Major=['']
# Score=['']
# Contributer=['胡艺凡']
# for i in result:
#     if(i):
#         City_result = re.split(r'cityName:', i)[1].split(r',')[0]
#         Province[0]=City_result
#         major=re.split(r'major:', i)[1].split(r',')[0]
#         Major[0]=major
#         category = re.split(r'subject:', i)[1].split(r',')[0]
#         if(int(category)==0):
#             Category[0]='理科'
#         if(int(category)==1):
#             Category[0]='文科'
#         year=re.split(r'year:', i)[1].split(r',')[0]
#         Year[0]=year
#         score=re.split(r'culturalMinScore:', i)[1].split(r',')[0]
#         Score[0]=score
#         row=[]
#         row.append(College[0])
#         row.append(Year[0])
#         row.append(Province[0])
#         row.append(Category[0])
#         row.append(Major[0])
#         row.append(Score[0])
#         row.append(Contributer[0])
#         rows.append(row)
# print(rows)
# print(result)
# print(soup)
