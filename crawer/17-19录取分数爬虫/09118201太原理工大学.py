import requests
from bs4 import BeautifulSoup
import csv

contributor = '09118201刘漪琛'
#create the csv file
f = open('09118201刘漪琛-太原理工大学.csv','w',encoding='utf-8',newline='')
#f.write(codecs.BOM_UTF8)
csv_writer = csv.writer(f)
csv_writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])

#list of request headers
header_list = [
    {'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Cookie': 'JSESSIONID=EE02C10063BCEBE1B2DD7AEFE894EC8D; Hm_lvt_db4fa75c98e225806c2ab6136b72708e=1589808698; Hm_lpvt_db4fa75c98e225806c2ab6136b72708e=1589808698',
    'Host': 'zs.tyut.edu.cn',
    'Referer': 'http://zs.tyut.edu.cn/info/1005/1326.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
    {'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Cookie': 'Hm_lvt_db4fa75c98e225806c2ab6136b72708e=1589808698; JSESSIONID=A54F6EC3AE44583FD32B4465D232BF34',
    'Host': 'zs.tyut.edu.cn',
    'Referer': 'http://zs.tyut.edu.cn/info/1005/1277.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
    {'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Cookie': 'Hm_lvt_db4fa75c98e225806c2ab6136b72708e=1589808698; JSESSIONID=063040C1EA5B2B1705A2392FDCF25AA6',
    'Host': 'zs.tyut.edu.cn',
    'Referer': 'http://zs.tyut.edu.cn/info/1005/1278.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
]

#list of urls
url_list = [
    "http://zs.tyut.edu.cn/info/1005/1326.htm",
    "http://zs.tyut.edu.cn/info/1005/1277.htm",
    "http://zs.tyut.edu.cn/info/1005/1278.htm"
]

province_list = ['内蒙古','辽宁','吉林','黑龙江','广西','四川','陕西','新疆','西藏']

#crawling the information in 2018
response1 = requests.get(url_list[0],headers=header_list[0])
response1.encoding = 'utf-8'
soup = BeautifulSoup(response1.text,'lxml')
#print(soup)

records = [[] for i in range(40)]
#print(records)
title = soup.find('title').get_text()
year = title[6:10]
print(year)

#get required information in html file
table = soup.find('table')
trs = table.find_all_next('tr')
i = 0
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        try:
            content = td.find('p').get_text()
            #print(content)
            if (content[-1] in ['市','省'] or content in province_list) and (content != '省市'):
                i += 1
                records[i].append(content)

            else:
                records[i].append(content)

        except AttributeError as e:
            continue

#write csv files with required information in fixed format
for k in range(1,len(records)):
    if records[k]:
        #print(records[k])
        record = records[k]
        temp = ['太原理工大学',year,record[0],'','all',0,contributor]
        temp1 = ['太原理工大学',year,record[0],'理科','all',0,contributor]
        temp2 =['太原理工大学',year,record[0],'文科','all',0,contributor]

        if record[0] == '上海市':
            temp[-2] = record[-1]
            print(temp)
            csv_writer.writerow(temp)
        elif (year != '2016') and (record[0] == '浙江省'):
            temp[-2] = record[7]
            print(temp)
            csv_writer.writerow(temp)
        else:
            selection = ['本科一批','本科一批A','本科一批B']
            for j in range(len(record)):
                if (record[j] in selection) and (record[j+1] == '理工类'):
                    temp1[-2] = record[j+5]
                    print(temp1)
                    csv_writer.writerow(temp1)
                    if (j+6 < len(record)) and (record[j+6] == '文史类'):
                        temp2[-2] = record[j+10]
                        print(temp2)
                        csv_writer.writerow(temp2)
                        break

                elif (record[j] in selection) and (j+6 < len(record)) and (record[j+6] == '理工类'):
                    temp1[-2] = record[j+10]
                    print(temp1)
                    csv_writer.writerow(temp1)
                    temp2[-2] = record[j+15]
                    print(temp2)
                    csv_writer.writerow(temp2)

#crawling the information in 2017
response2 = requests.get(url_list[1],headers=header_list[1])
response2.encoding = 'utf-8'
soup = BeautifulSoup(response2.text,'lxml')
#print(soup)

records = [[] for i in range(40)]
#print(records)
title = soup.find('title').get_text()
year = title[6:10]
print(year)

#get required information in html file
table = soup.find('table')
trs = table.find_all_next('tr')
i = 0
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        try:
            content = td.find('p').find('span').get_text()
            #print(content)
            if (content[-1] in ['市','省'] or content in province_list) and (content != '省市'):
                i += 1
                records[i].append(content)

            else:
                records[i].append(content)

        except AttributeError as e:
            continue

#write csv file with required information in fixed format
for k in range(1,len(records)):
    if records[k]:
        #print(records[k])
        record = records[k]
        temp = ['太原理工大学',year,record[0],'','all',0,contributor]
        temp1 = ['太原理工大学',year,record[0],'理科','all',0,contributor]
        temp2 =['太原理工大学',year,record[0],'文科','all',0,contributor]

        if record[0] == '上海市':
            temp[-2] = record[-1]
            print(temp)
            csv_writer.writerow(temp)
        elif (year != '2016') and (record[0] == '浙江省'):
            temp[-2] = record[7]
            print(temp)
            csv_writer.writerow(temp)
        else:
            selection = ['本科一批','本科一批A','本科一批B']
            for j in range(len(record)):
                if (record[j] in selection) and (record[j+1] == '理工类'):
                    temp1[-2] = record[j+5]
                    print(temp1)
                    csv_writer.writerow(temp1)
                    if (j+6 < len(record)) and (record[j+6] == '文史类'):
                        temp2[-2] = record[j+10]
                        print(temp2)
                        csv_writer.writerow(temp2)
                        break

                elif (record[j] in selection) and (j+6 < len(record)) and (record[j+6] == '理工类'):
                    temp1[-2] = record[j+10]
                    print(temp1)
                    csv_writer.writerow(temp1)
                    temp2[-2] = record[j+15]
                    print(temp2)
                    csv_writer.writerow(temp2)

#crawling the information in 2016
response3 = requests.get(url_list[2],headers=header_list[2])
response3.encoding = 'utf-8'
soup = BeautifulSoup(response3.text,'lxml')
#print(soup)

records = [[] for i in range(40)]
#print(records)
title = soup.find('title').get_text()
year = title[6:10]
print(year)

#get required information in html file
table = soup.find('table')
trs = table.find_all_next('tr')
i = 0
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        try:
            content = td.find('p').find('span').get_text()
            #print(content)
            if (content[-1] in ['市','省'] or content in province_list) and (content != '省市'):
                i += 1
                records[i].append(content)

            else:
                records[i].append(content)

        except AttributeError as e:
            continue

#write csv file with required information in fixed format
for k in range(1,len(records)):
    if records[k]:
        #print(records[k])
        record = records[k]
        temp = ['太原理工大学',year,record[0],'','all',0,contributor]
        temp1 = ['太原理工大学',year,record[0],'理科','all',0,contributor]
        temp2 =['太原理工大学',year,record[0],'文科','all',0,contributor]

        if record[0] == '上海市':
            temp[-2] = record[-1]
            print(temp)
            csv_writer.writerow(temp)
        elif (year != '2016') and (record[0] == '浙江省'):
            temp[-2] = record[7]
            print(temp)
            csv_writer.writerow(temp)
        else:
            selection = ['本科一批','本科一批A','本科一批B']
            for j in range(len(record)):
                if (record[j] in selection) and (record[j+1] == '理工类'):
                    temp1[-2] = record[j+5]
                    print(temp1)
                    csv_writer.writerow(temp1)
                    if (j+6 < len(record)) and (record[j+6] == '文史类'):
                        temp2[-2] = record[j+10]
                        print(temp2)
                        csv_writer.writerow(temp2)
                        break

                elif (record[j] in selection) and (j+6 < len(record)) and (record[j+6] == '理工类'):
                    temp1[-2] = record[j+10]
                    print(temp1)
                    csv_writer.writerow(temp1)
                    temp2[-2] = record[j+15]
                    print(temp2)
                    csv_writer.writerow(temp2)

f.close()