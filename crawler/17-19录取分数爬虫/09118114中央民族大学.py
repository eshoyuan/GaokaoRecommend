import requests
import re
import csv

url='https://zb.muc.edu.cn/query_findAdmissionScorePageList.json'#招生信息url

def getHTMLText(url):#获取url内容的函数
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return "产生异常"

r=getHTMLText(url)#获得response对象

rule1 = '\[(.*?)\]'

message=re.findall(rule1,r.text)#在r.text中提取出招生信息


rule2 = '{(.*?)}'

data=re.findall(rule2,str(message))#在招生信息中获得各个单项

f=open('中央民族大学招生信息.csv','w',encoding='utf-8')#创建CSV文件

csv_writer = csv.writer(f)

csv_writer.writerow(["College","Year",'Province','Category','Major','MaxScore','MinScore','AvgScore','Contributor'])#写入表头

#写入每行内容
for i in data:
    csv_writer.writerow(['中央民族大学',re.findall('year":"(.*?)"',i),re.findall('sfmc":"(.*?)"',i),re.findall('klmc":"(.*?)"',i)
                             ,re.findall('zymc":"(.*?)"',i),re.findall('maxcj":(.*?),',i),re.findall('mincj":(.*?),',i),
                            re.findall('avgcj":(.*?),',i),'09118114_周吾君'])





