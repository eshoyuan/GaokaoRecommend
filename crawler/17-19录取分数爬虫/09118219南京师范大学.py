import requests
from bs4 import BeautifulSoup
import pandas as pd

#根据url来爬取指定网址的信息 并返回列表形式
def get_data(url):
    #存储列表
    data=[]
    #爬取数据
    req=requests.get(url, headers=headers1,timeout=(3,7))
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'lxml')
    detail = soup.find_all('tr', class_='tb_info_all_content')
    #循环得到每一年的不同专业分数线
    for i in range(len(detail)):
        temp_list=detail[i].find_all('td')
        #该网页没有数据
        if(temp_list[0].text=='暂无数据'):
            return None
        #寻找本一批次数据
        elif (temp_list[4].get_text()=='本一' or temp_list[4].get_text()=='本一批次'):
            temp=[]
            #年份
            temp.append(temp_list[0].get_text())
            #统一省市的名称，都不带‘省，市’
            if(temp_list[1].get_text()!='内蒙古' and temp_list[1].get_text()!='黑龙江'):
                temp.append(temp_list[1].get_text()[0:2])
            else:
                temp.append(temp_list[1].get_text())

            #科类
            temp.append(temp_list[3].get_text())
            #专业
            temp.append(temp_list[2].get_text())
            #录取最低分
            temp.append(temp_list[6].get_text())
            #把结果列表存起来
            data.append(temp)
    return data

#根据年份和省份制定特别的爬取函数，返回列表 据此也可以轻松得到2016年数据
def solution_to_change(data,original,year,province):
    for i in year:
        for j in province:
            k = 1
            #静态网页的改变
            url_present=original+'NF='+i+'&SF='+j
            #没有数据
            if(get_data(url_present + '&page=' + str(k))==None):
                continue
            else:
                data += get_data(url_present + '&page=' + str(k))
                #读取不同页数的数据，如果只有一页就读一页
                while(get_data(url_present+'&page='+str(k))!=get_data(url_present+'&page='+str(k+1))):
                    data+=get_data(url_present+'&page='+str(k+1))
                    k+=1
    return data

#基础网址
original1 = 'http://bkzs.njnu.edu.cn/fsx?'
#2019在本网址与前两个结果不同 可以分开考虑
year1=['2017','2018']
province1=['上海','云南','内蒙古','内蒙','北京','吉林','四川','天津','宁夏','安徽','山东','山西','广东','广西','江西','新疆','江苏','江西','河北','河南','浙江','海南',
           '湖北','湖南','甘肃','福建','贵州','辽宁','重庆','陕西','青海','黑龙江']

year2=['2019']
#网站设置特殊性，2019年全部带上了‘省市’
province2=['上海市','云南省','内蒙古','北京市','吉林省','四川省','天津市','宁夏','安徽省','山东省','山西省','广东省','广西省','江西省','新疆','江苏省','江西省','河北省','河南省','浙江省','海南省',
           '湖北省','湖南省','甘肃省','福建省','贵州省','辽宁省','重庆市','陕西省','青海省','黑龙江']

#头文件
headers1={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID2=8crfjb0b7822s0cmv0bnp82h24; Hm_lvt_b3b075d90cc24dcb1d5795260f02e2d6=1589811268,1589811419,1589869726,1589891859; Hm_lpvt_b3b075d90cc24dcb1d5795260f02e2d6=1589891859',
'Host': 'bkzs.njnu.edu.cn',
'Referer': 'http://bkzs.njnu.edu.cn/fsx',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'}

data1=[]
data=solution_to_change(data1,original1,year1,province1)
#最终结果列表
data_result=solution_to_change(data,original1,year2,province2)

#转化为dataframe
data_df = pd.DataFrame(data_result, columns=["Year","Province","Category","Major","Score"])
#增加表格数据
data_df.insert(0,'College',"南京师范大学")
data_df["Contributor"]="09118219王一名"

#保存表格excel
data_df.to_csv("09118219王一名-南京师范大学.csv",index=False,encoding='gbk',sep=',')