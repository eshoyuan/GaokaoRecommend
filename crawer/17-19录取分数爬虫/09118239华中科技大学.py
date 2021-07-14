import requests
import pandas as pd
from bs4 import BeautifulSoup

branch = ['理工','文史','综合改革']
year = ['2017','2018','2019']
province = ['北京市','天津市','河北省','山西省','内蒙古自治区','辽宁省','吉林省','黑龙江省',
            '上海市','江苏省','浙江省','安徽省','福建省','江西省','山东省','河南省','湖北省',
            '湖南省','广东省','广西壮族自治区','海南省','重庆市','四川省','贵州省','云南省','西藏自治区',
           '陕西省','甘肃省','青海省','宁夏回族自治区','新疆维吾尔自治区']

url = 'http://zsb.hust.edu.cn/fsflqfsx.jsp?wbtreeid=1261'
# 火狐浏览器请求头
data = {'Host':'zsb.hust.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '60',
        'Origin': 'http://zsb.hust.edu.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://zsb.hust.edu.cn/fsflqfsx.jsp?wbtreeid=1261',
        'Cookie': 'JSESSIONID=A82BB35110CB3E19247D7FF6260BB67D',
        'Upgrade-Insecure-Requests': '1',
        'kl': '',   #文理分类
        'nf': '',   #年份
        'sf': ''    #省份
        }

#存储全部数据的表格，College和Contributor后续添加
table = pd.DataFrame(columns = ['Year','Province','Category','Major','Score'])

for j in range(len(year)):  #选择年份
    data['nf'] = year[j]
    for i in range(len(branch)):    #选择文理分类
        data['kl'] = branch[i]
        for k in range(len(province)):  #选择省份
            data['sf'] = province[k]
            response = requests.post(url,data)
            bs = BeautifulSoup(response.text,'lxml')    #解析response对象
            infor = bs.find_all('td')   #所需的信息标签为<td>       infor为由tag组成的list
            for m in range(len(infor)):
                infor[m] = infor[m].string  #去除html格式符号，仅留下所需的字符信息

            #将信息添加到table里
            for m in range(0,len(infor),4):
                if infor[m] == '普通一批':
                     table.loc[len(table)] = [year[j],province[k],branch[i],infor[m+1],infor[m+2]]

table.insert(0,'College','华中科技大学')  #插入第一列College
table['Contributor'] = '09118239赵琦' #插入最后一列Contributor
table.to_csv('HUST.csv',encoding='utf-8-sig',index=None)    #保存为csv文件，utf-8格式excel打开中文乱码，需要utf-8-sig格式