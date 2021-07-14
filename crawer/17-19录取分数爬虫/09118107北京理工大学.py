import requests
import pandas as pd
import csv
import string
from bs4 import BeautifulSoup as bs

#准备工作
url="http://admission.bit.edu.cn/signup/scoreQuery.do"
pro_headers={"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "__jsluid_h=018666eaa3e0b7a879f42eb64d4987ec; __51cke__=; JSESSIONID=AC202B07174D17593539666A303B020A; ms.session.id=ae82bc94-2eca-48ef-8833-9dffc7e623e1; __tins__19991633=%7B%22sid%22%3A%201590316147131%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201590318950166%7D; __51laig__=10",
"Host": "admission.bit.edu.cn",
"Origin": "http://admission.bit.edu.cn",
"Referer": "http://admission.bit.edu.cn/html/1/168/172/index.html",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"}
year=["2019","2018","2017"]
page19=[]
page18=[]
page17=[]
for i in range(35):
    page19.append(i+1)
for i in range(32):
    page18.append(i+1)
for i in range(61):
    page17.append(i+1)
carrier=[]
temp=[]
temp_for_year=[]
keys=["year","province","type","major","minimum"]

#爬虫代码
for y in year:
    if y=="2019":
        temp_for_year=page19
    elif y=="2018":
        temp_for_year=page18
    else:
        temp_for_year=page17
    for i in temp_for_year:
        pro_data={"sortOrder":"desc","pageSize":"10","pageNumber":i,"year":y}
        request=requests.post(url=url,data=pro_data,headers=pro_headers)
        request.encoding='utf-8'
        response=json.loads(request.text)
        for e in response['rows']:
            temp.append("北京理工大学")
            for k in keys:
                temp.append(e[k])
            temp.append("09118107徐子轩")
            carrier.append(temp)
            temp=[]

#生成csv文件
file_path="09118107 徐子轩-东南大学.csv"
csvFile=open(file_path,"w")
writer=csv.writer(csvFile)
writer.writerow(["College","Year","Province","Category","Major","Score","Contributor"])
for i in carrier:
    writer.writerow(i)
csvFile.close()
print("Finished!!!")
