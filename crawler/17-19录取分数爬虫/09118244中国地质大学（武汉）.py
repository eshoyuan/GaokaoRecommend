import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs

College='中国地质大学（武汉）'
Contributor='09118244尹行健'
dataframe=[]#暂时存储爬取的数据（list格式）

'''
待爬取网页为
http://zhinengdayi.com/page/detail/AIGTAZ/10518/1012
该网页有五个combobox，
根据观察和F12后的进程显示，
‘录取批次’选项对数据结果并无影响，
选项内容‘生源地’、‘年度’、‘科类’、‘类型’依顺序初始化，
且‘生源地’的不同会导致‘年度’、‘科类’和‘类型’的初始化不同。
所以考虑首先依次爬取各个combobox的初始化结果，
再爬取不同‘生源地’、‘年度’、‘科类’、‘类型’条件下的分数线信息
'''

#爬取‘生源地’初始化信息
address='http://admin.zhinengdayi.com/front/info/form/majorScore'
post={}
post['sCode']='AIGTAZ'
post['showDetailsConfig']='2'
response=requests.post(address,data=post)
response=bs(response.text,'lxml')
response=response.find('select')
patt=re.compile(r'<option.+?>(.+?)</option>')
Provinces=patt.findall(str(response))

for province in Provinces:
    #爬取‘年度’和‘科类’初始化信息
    address='http://admin.zhinengdayi.com/front/enroll/getMajorSelectChange'
    post={}
    post['sCode']='AIGTAZ'
    post['cityName']=province
    response=requests.post(address,data=post)
    response=response.json()
    #得到当前‘生源地’下‘年度’和‘科类’的初始化信息
    temp_category=response['scienceList']
    temp_year=response['yearList']
    for each_category in temp_category:
        #网站中以‘理工’表示‘理科’，‘文史’表示‘文科’，这里进行一个转换
        if each_category=='理工':
            category='理科'
        elif each_category=='文史':
            category='文科'
        else:
            category='all'
        
        for each_year in temp_year:
            #爬取‘类型’初始化信息
            address='http://admin.zhinengdayi.com/front/enroll/getMajorSelectChange'
            post={}
            post['sCode']='AIGTAZ'
            post['cityName']=province
            post['year']=each_year
            post['scienceClass']=each_category
            response=requests.post(address,data=post)
            response=response.json()
            #得到当前‘生源地’、‘年度’和‘科类’下‘类型’的初始化信息
            temp_type=response['typeList']
            for each_type in temp_type:
                address='http://admin.zhinengdayi.com/front/enroll/findMajorScoreList'
                post['type']=each_type
                response=requests.post(address,data=post)
                response=response.json()
                temp_major=response['list']
                for each_major in temp_major:
                    #爬取当前‘生源地’、‘年度’、‘科类’和‘类型’下的成绩信息
                    temp=[College,each_year,province,category,each_major['majorName'],each_major['lowScore'],Contributor]
                    dataframe.append(temp)

#将数据转换为DataFrame并储存到csv文件
scoredata=pd.DataFrame(dataframe,columns=['College','Year','Province','Category','Major','Score','Contributor'])
filename=Contributor+'-'+College+'.csv'
scoredata.to_csv(filename,sep=',',encoding='utf_8_sig')
