import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
headers={
  'user-agent':'Mozilla/5.0'
}#模拟浏览器进行爬取

url = 'https://zsjyc.ysu.edu.cn/bkszsxxw/lnfsx.jsp?wbtreeid=1019'

def vis(url,dic):
 req=requests.post(url,dic)
 req.raise_for_status()
 req.encoding = req.apparent_encoding#内容获取的内容进行转码，以防出现乱码的情况。    
 # print(html.text)
 soup = BeautifulSoup(req.text,'html.parser')
 tmplist =str( soup)#获取第一页href相关的位置

 
 tmplist=re.findall( r'(?<=">).*?(?=</td)',tmplist)

 for i in range(len(tmplist)):
    if tmplist[i]=='历年分数线':
        tmplist=tmplist[i+2:len(tmplist)-2:]
        break
 name=tmplist[:8:]
 tmplist=tmplist[8::]

 res=[]
 for i in range(0,len(tmplist),8):
    res.append(tmplist[i:i+8:])
 return name ,res

def get_prov_year_list(url):
    r=url
    html = requests.get(r,headers=headers)
    html.raise_for_status()
    html.encoding = html.apparent_encoding#内容获取的内容进行转码，以防出现乱码的情况。    
    soup = BeautifulSoup(html.text,'html.parser')
    tmplist = soup.find_all('a','pro')#获取第一页href相关的位置
    provence_list=[]
    for item in tmplist:
        rawdata = item['href']
        chinese_pattern = '[\u4e00-\u9fa5]+'
        rawdata = re.findall(chinese_pattern, rawdata)
        provence_list.append(rawdata)
    year_list=[]
    tmplist = soup.find_all('a','year')#获取第一页href相关的位置
    for item in tmplist:
        rawdata = item['href']
        pattern = '2\d+\.?\d*'
        rawdata = re.findall(pattern, rawdata)
        year_list.append(rawdata)
    return provence_list,year_list 
def getdata(provence_list,year_list):
 dic={}
 result=[]
 for j in year_list:
    for i in provence_list:
        dic={'pro':i,'year':j}
        name,res=vis(url,dic)
        for item in res:
            item.append('燕山大学')
            item.append(j)
            item.append('09118129陈翼张')
        result.append(res)
 result=sum(result,[])
 name=['Province',	'Major',	'Category'	,'最高分'	,'Score','平均分',	'人数'	,'一本线	','College'	,'Year','Contributor']
 test=pd.DataFrame(columns=name,data=result)
 return test
def data_washer(test):   
 name=['最高分'	,'平均分',	'人数'	,'一本线	']
 test=test.drop(name,axis=1)
 name=['College'	, 'Year'	,'Province','Category'	,'Major',	'Score','Contributor']
 test = test.loc[:,name]
 return test
def run_web_crawler():
    provence_list,year_list = get_prov_year_list(url)
    year_list=sum(year_list,[])
    provence_list=sum(provence_list,[])
    test=data_washer(getdata(provence_list,year_list))
    test.to_csv('./09118129陈翼张-燕山大学.csv',index=False)
if __name__ == '__main__':
    run_web_crawler()