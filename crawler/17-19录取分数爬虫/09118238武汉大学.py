"""
Homework1
made in May 22nd,2020
@author: linXin 09118238
"""
import urllib3
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup

url='http://210.42.122.133/fsb/'
pro_list=['北京市','福建省','甘肃省','港澳台联招','广东省','广西区',
          '贵州省','海南省','河北省','河南省','黑龙江','湖北省',
          '湖南省','吉林省','江苏省','江西省','辽宁省','内蒙古',
          '宁夏区','青海省','山东省','山西省','陕西省','上海市','四川省',
          '天津市','新疆区','云南省','浙江省','重庆市']
year_list=['2019','2018','2017','2016']
USER_AGENTS=[
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'
]
headers1 = {
    'User-Agent': random.choice(USER_AGENTS)
}

def get_data(pro,year):
    '''
    对网站动态表格抓取数据，输入年份与省份，返回对应的表格
    '''
    data1={
    'year':year,
    'shengfen':pro,
    'kl':'',
    'enews': 'cx',
    'Submit': '查询'
    }
    r=requests.post(url,data=data1,headers=headers1)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'html.parser')
    tables = soup.findAll('table') #定位选择网站的所有表格
    tab = tables[2] #选择网站的第二个表格
    data_list = [] #存放表格每行内容
    for tr in tab.findAll('tr'):
        str=''
        for i,td in enumerate(tr.findAll('td')):
            if i==4 or i==6 or i==7:#跳过不需要的列
                continue
            str+=td.getText()
        data_list.append(str.split())
    data_cut=data_list[2:len(data_list)-1] #观察前面输出结果，去掉首尾两个多余列
    return data_cut

all_list=[] #存放某年某省的表格
for year in range(0,len(year_list)):
    for province in range(0,len(pro_list)):
        all_list.append(get_data(pro_list[province],year_list[year]))

#将表格连续追加存入csv文件
for i in range(0,len(all_list)):
    df=pd.DataFrame(all_list[i]) #转换成DataFrame
    df1=df.rename(columns={0:'Year',1:'Province',2:'Category',3:'Major',4:'Score'}) #重新命名列
    df1['College']='武汉大学' #补充两列内容
    df1['Contributor']='09118238林欣'
    df2=df1.reindex(columns=['College','Year','Province','Category','Major','Score','Contributor']) #对列重新排序
    if i==0:
        df2.to_csv('09118238林欣_武汉大学.csv',mode='a',index=0)
    else:
        df2.to_csv('09118238林欣_武汉大学.csv',mode='a',index=0,header=0)   #除第一份以外其他不保存列名