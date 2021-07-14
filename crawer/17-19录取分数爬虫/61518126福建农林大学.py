from bs4 import BeautifulSoup
import requests
# import parsel
import csv

url_17='http://zsb.fafu.edu.cn/2017/0907/c379a45661/page.htm'
url_18='http://zsb.fafu.edu.cn/2018/0820/c379a45670/page.htm'
url_19='http://zsb.fafu.edu.cn/2019/0927/c379a47103/page.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
 'Referer': 'http://zsb.fafu.edu.cn/379/list2.htm',
'Cookie': 'JSESSIONID=EC847A5744357AB72B3506130822592A'}
response_17 = requests.get(url_17, headers=headers)
response_17.encoding = response_17.apparent_encoding
# 爬取17
soup_17 = BeautifulSoup(response_17.text, 'lxml')
trs_17 = soup_17.find_all('td')
response_18 = requests.get(url_18, headers=headers)
response_18.encoding = response_18.apparent_encoding
# 爬取18
soup_18 = BeautifulSoup(response_18.text, 'lxml')
trs_18 = soup_18.find_all('td')
response_19 = requests.get(url_19, headers=headers)
response_19.encoding = response_19.apparent_encoding
# 爬取19
soup_19 = BeautifulSoup(response_19.text, 'lxml')
trs_19 = soup_19.find_all('td')

# 内容存储到列表内
list_17=[]
list_18=[]
list_19=[]
for tr in trs_17:
    ui = []
    for ts in tr:
        ui.append(ts.string)
    # print (ui)
    list_17.append(ui)
for tr in trs_18:
    ui = []
    for ts in tr:
        ui.append(ts.string)
    # print (ui)
    list_18.append(ui)
for tr in trs_19:
    ui = []
    for ts in tr:
        ui.append(ts.string)
    # print (ui)
    list_19.append(ui)

# 去掉无用内容
List_17= list_17[19:5035]
List_18= list_18[19:4451]
List_19= list_19[18:4458]

# 写入csv
with open("61518126杜宇涵-福建农林大学.csv", 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['School', 'Year', 'Province', 'Class', 'Category', 'Major', 'Score', 'Contributor'])
    for i in range(int(len(List_17)/8)):
        if List_17[8*i+2][0].find('二') < 0:
            writer.writerow(['福建农林大学', List_17[8*i][0], List_17[8*i+1][0], List_17[8*i+2][0], List_17[8*i+3][0], List_17[8*i+4][0], List_17[8*i+5][0], '61818126杜宇涵'])
            i = +1
        else:

            i = i+1
    for i in range(int(len(List_18)/8)):
        if List_18[8*i+2][0].find('二') < 0:
            writer.writerow(['福建农林大学', List_18[8*i][0], List_18[8*i+1][0], List_18[8*i+2][0], List_18[8*i+3][0], List_18[8*i+4][0], List_18[8*i+5][0], '61818126杜宇涵'])
            i = +1
        else:

            i = i+1
    for i in range(int(len(List_19)/8)):
        if List_19[8*i+2][0].find('二') < 0:
            print(List_19[8*i+2][0] )
            writer.writerow(['福建农林大学', List_19[8*i][0], List_19[8*i+1][0], List_19[8*i+2][0], List_19[8*i+3][0], List_19[8*i+4][0], List_19[8*i+5][0], '61818126杜宇涵'])
            i = +1
        else:

            i = i+1
