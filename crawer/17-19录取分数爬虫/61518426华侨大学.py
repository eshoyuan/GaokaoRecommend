'''
Created by Ononoki_Yotsugi
On 2020.5.23
爬取华侨大学近三年本科普通类的录取数据
注：华侨大学对福建、福建泉州、福建厦门分开招生
'''

import requests
import csv
from bs4 import BeautifulSoup


requests.packages.urllib3.disable_warnings()   #忽略SSL的警告
#根据要求用来筛选出理科、文科、综合的字典
category_dic={'理工':'理科','文史':'文科','理科':'理科','文科':'文科','普通理科':'理科','普通文科':'文科',
              '理科综合':'理科','文科综合':'文科','文史类':'文科','理工类':'理科','综合改革':'all',
              '文科普通类':'文科','理科普通类':'理科'}
#根据要求用来筛选出本科普通类的列表
batches=['本科','本科A批','本科第一批','本科批','本科批次A阶段','本科普通批','本科一批','本科一批普通类',
         '本科一批院校A段','单设本科','第一批A段','第一批本科','第一批本科B类','普通类','一本','一本1/单设本科',
         '一批本科']

def GetHtml(url):
    #对传入的url页面内容进行爬取
    try:
        r=requests.get(url,headers={'user-agent':'Mozilla/5.0'},timeout=30,verify=False)
        #这里需要使用verify=False关闭SSL安全验证
        r.encoding=r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print('error')
        return ""

def GetInfo(html,year,province):
    #对某个年份省份页面内容进行解析，抽取出需要的数据
    list=[]
    soup=BeautifulSoup(html,'html.parser')
    if soup:
        tuples=soup.find_all('tr',{'height':True})   #<tr></tr>中包含一行
        if tuples:
            location=[]   #用来保存‘专业名称’等信息在<tr></tr>中的位置（因为对于不同年份不同省份可能不一致）
            for i,tuple in enumerate(tuples):   #<td></td>中包含一个属性值
                tds=tuple.find_all('td')
                if not location:
                    #location为空，位置未获取，同时可以跳过前边一些无用的<tr></tr>
                    for j,td in enumerate(tds):
                        if td.text=='专业名称':
                            location.append(j)
                        elif td.text=='批次名称':
                            location.append(j)
                        elif td.text=='科类名称':
                            location.append(j)
                        elif td.text == '最低分':
                            location.append(j)
                else:
                    if len(tds)<location[-1]+1:
                        #<tr></tr>中<td></td>过少，可以跳过无效的<tr></tr>
                        continue
                    name=tds[location[0]].text
                    batch=tds[location[1]].text
                    if not batch in batches:
                        #筛选批次
                        continue
                    category=category_dic.get(tds[location[2]].text)
                    if not category:
                        #筛选科类
                        continue
                    lowest=tds[location[3]].text
                    list.append(('华侨大学',year,province,name,category,lowest,'61518426周之遥'))
        else:print('error')
    return list

list=[]
#网页上用于标记不同省份的缩写及其全名
provinces={'bj':'北京','tj':'天津','hbei':'河北','sx':'山西','nmg':'内蒙古','ln':'辽宁','jl':'吉林','hlj':'黑龙江','sh':'上海','js':'江苏','zj':'浙江',
           'ah':'安徽','fjs':'福建','fjqz':'福建泉州','fjxm':'福建厦门','jx':'江西','sd':'山东','hnan':'河南','hb':'湖北','hn':'湖南','gd':'广东',
           'gx':'广西','hain':'海南','cq':'重庆','sc':'四川','gz':'贵州','yn':'云南','sxi':'陕西','gs':'甘肃','qh':'青海','nx':'宁夏','xj':'新疆'}
for year in [2019,2018,2017]:
    for abbreviate, province in provinces.items():
        print('Begin crawling',year,province)
        url='https://zsc.hqu.edu.cn/zsb/lqqk/'+abbreviate+'.files/sheet00'+str(year-2014)+'.htm'   #不同年份不同省份的url有一定规律
        html=GetHtml(url)
        newlist=GetInfo(html,year,province)
        list.extend(newlist)

with open('data.csv','w',newline='',encoding='utf-8') as f:
    cw= csv.writer(f)
    title = ['College','Year','Province','Category','Major','Score','Contributor']
    cw.writerow(title)
    for i in list:
        cw.writerow(i)
