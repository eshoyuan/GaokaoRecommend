import requests
import json
import time
import pandas as pd

def get_nationwide_1(df, year):
    df1 = df[1]
    df1['College'], df1['Year'], df1['Major'], df1['Category'] = '上海外国语大学', str(year), 'all', None
    df1.drop([0, 1, 2], axis = 0, inplace = True)
    newframe = pd.DataFrame()
    for index,row in df1.iterrows():
        if (row[1] == '本科批' or row[1] == '本一批'):
            score1 = row[4]                 #文科最低分
            row['Category'] = '理科'
            newframe = newframe.append(row)
            row[8] = score1
            row['Category'] = '文科'
            newframe = newframe.append(row)
    order = ['College', 'Year', 0, 'Category', 'Major', 8]
    newframe = (newframe)[order]
    newframe.columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score']
    return newframe

def get_nationwide_2(df, year, strings):
    df1 = df[1]
    df1['College'], df1['Year'], df1['Major'], df1['Category'] = '上海外国语大学', str(year), 'all', None
    df1.drop([0, 1, 2], axis = 0, inplace = True)
    newframe = pd.DataFrame()   
    is_bachelor = 0                         #是否为本科批        
    for index, row in df1.iterrows():       #数据整理
        if(row[0] == strings):
            is_bachelor = 1
            row[0] = row[1]
            row[3] = row[4]
            row[7] = row[8]
        else:
            if is_bachelor != 1:
                continue
        if is_bachelor == 1:
            score1 = row[3]                 #文科最低分
            row['Category'] = '理科'
            newframe = newframe.append(row)
            row[7] = score1
            row['Category'] = '文科'
            newframe = newframe.append(row)
    order = ['College', 'Year', 0, 'Category', 'Major', 7]
    newframe = (newframe)[order]
    newframe.columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score']
    return newframe

def get_shanghai_1(df, year):
    df2 = df[2]
    df2.drop([0, 1], inplace = True)
    df2['College'], df2['Year'], df2['Province'], df2['Category'] = '上海外国语大学', str(year), '上海', 'all'
    newframe2 = pd.DataFrame()
    is_bachelor = 0                         #是否为本科批        
    for index, row in df2.iterrows():       #数据整理
        if(row[0] == '合计'):
            is_bachelor = 0
        if is_bachelor == 1:
            newframe2 = newframe2.append(row)
        if(row[0] == '本科批'):
            is_bachelor = 1
            row[0] = row[1]
            row[3] = row[4]
            newframe2 = newframe2.append(row)   
    order = ['College', 'Year', 'Province', 'Category', 0, 3] 
    newframe2 = newframe2[order]
    newframe2.columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score']
    return newframe2

def get_zhejiang_1(df, year, strings):
    df3 = df[3]
    df3.drop([0, 1], inplace = True)
    df3['College'], df3['Year'], df3['Province'], df3['Category'] = '上海外国语大学', str(year), '浙江', 'all'
    newframe3 = pd.DataFrame()
    is_bachelor = 0                         #是否为本科批        
    for index, row in df3.iterrows():       #数据整理
        if(row[0] == '合计'):
            is_bachelor = 0
        if is_bachelor == 1:
            newframe3 = newframe3.append(row)
        if(row[0] == strings):
            is_bachelor = 1
            row[0] = row[1]
            row[3] = row[4]
            newframe3 = newframe3.append(row) 
    order = ['College', 'Year', 'Province', 'Category', 0, 3] 
    newframe3 = newframe3[order]
    newframe3.columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score']
    return newframe3

def get_shanghai_zhejiang(df, year, strings, select):
    df1 = df[select]
    df1['College'], df1['Year'], df1['Major'], df1['Category'], df1['Province'] = '上海外国语大学', str(year), 'all', None, None
    df1.drop([0, 1, 2], axis = 0, inplace = True)
    newframe = pd.DataFrame()   
    is_bachelor = 0                         #是否为本科批        
    for index, row in df1.iterrows():       #数据整理
        if(row[0] == '总计'):
            continue
        if(row[0] == strings):
            is_bachelor = 1
            row[0] = row[1]
            row[3] = row[4]
            row[7] = row[8]
        else:
            if is_bachelor != 1:
                continue
        if is_bachelor == 1:
            score1 = row[3]                 #文科最低分
            row['Category'] = '理科'
        if select == 2:
            row['Province']= '上海'
        if select == 3:
            row['Province']= '浙江'
        newframe = newframe.append(row)
        row[7] = score1
        row['Category'] = '文科'
        newframe = newframe.append(row)
    order = ['College', 'Year', 'Province', 'Category', 0, 7]
    newframe = (newframe)[order]
    newframe.columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score']
    return newframe

headers = []
headers.append({
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'JSESSIONID=2AF5707F6359EF9FA04FDF018D2EE4A8',
        'Host': 'admissions.shisu.edu.cn',
        'Origin': 'http://admissions.shisu.edu.cn',
        'Referer': 'http://admissions.shisu.edu.cn/dd/69/c633a122217/page.psp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    })
headers.append({
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'JSESSIONID=2AF5707F6359EF9FA04FDF018D2EE4A8',
        'Host': 'admissions.shisu.edu.cn',
        'Origin': 'http://admissions.shisu.edu.cn',
        'Referer': 'http://admissions.shisu.edu.cn/b2/e2/c633a111330/page.psp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    })
headers.append({
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'JSESSIONID=2AF5707F6359EF9FA04FDF018D2EE4A8',
        'Host': 'admissions.shisu.edu.cn',
        'Origin': 'http://admissions.shisu.edu.cn',
        'Referer': 'http://admissions.shisu.edu.cn/64/1c/c633a91164/page.psp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    })
headers.append({
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'JSESSIONID=2AF5707F6359EF9FA04FDF018D2EE4A8',
        'Host': 'admissions.shisu.edu.cn',
        'Origin': 'http://admissions.shisu.edu.cn',
        'Referer': 'http://admissions.shisu.edu.cn/50/7d/c633a86141/page.psp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    })

urls = ['http://admissions.shisu.edu.cn/dd/69/c633a122217/page.psp', 
       'http://admissions.shisu.edu.cn/b2/e2/c633a111330/page.psp',
       'http://admissions.shisu.edu.cn/64/1c/c633a91164/page.psp',
       'http://admissions.shisu.edu.cn/50/7d/c633a86141/page.psp']

result = pd.DataFrame()

#由于每年的表格都不太一样，所以此处没有用循环
year = 2019
time.sleep(1)
request = requests.get(url = urls[0], headers = headers[0])
htmls = request.text
df = pd.read_html(htmls)
newframe = get_nationwide_1(df, year)
newframe2 = get_shanghai_1(df, year)                   #获取上海市（特殊）数据
newframe3 = get_zhejiang_1(df, year, '第一段平行')     #获取浙江省（特殊）数据
result_2019 = pd.concat([newframe, newframe2, newframe3], axis = 0)

year = 2018
time.sleep(1)
request = requests.get(url = urls[1], headers = headers[1])
htmls = request.text
df = pd.read_html(htmls)
newframe = get_nationwide_2(df, year, '本一批(本科批)')
newframe2 = get_shanghai_1(df, year)
newframe3 = get_zhejiang_1(df, year, '第一段平行')
result_2018 = pd.concat([newframe, newframe2, newframe3], axis = 0)

year = 2017
time.sleep(1)
request = requests.get(url = urls[2], headers = headers[2])
htmls = request.text
df = pd.read_html(htmls)
newframe = get_nationwide_2(df, year, '本一批(本科批)')
newframe2 = get_shanghai_1(df, year)
newframe3 = get_zhejiang_1(df, year, '本科批')
result_2017 = pd.concat([newframe, newframe2, newframe3], axis = 0)

year = 2016
time.sleep(1)
request = requests.get(url = urls[3], headers = headers[3])
htmls = request.text
df = pd.read_html(htmls)
newframe = get_nationwide_2(df, year, '本一批')
newframe2 = get_shanghai_zhejiang(df, year, '本科批', 2)
newframe3 = get_shanghai_zhejiang(df, year, '本一批', 3)
result_2016 = pd.concat([newframe, newframe2, newframe3], axis = 0)

result = pd.concat([result_2019, result_2018, result_2017, result_2016], axis = 0)
result['Contributor'] = '09118132陈震寰'

result.to_csv('09118132陈震寰-上海外国语大学.csv', index = False, 
              columns = ['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])
