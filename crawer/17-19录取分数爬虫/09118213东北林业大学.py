from bs4 import BeautifulSoup
import requests
import csv
import copy

def get(url):#将url化为html
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    return html

def StrNum(str):#自写函数：提取字符串中的数字
    Num=''
    for i in str:
        if i >= '0' and i <= '9':
            Num+=i
    return Num

ProvinceList=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','江苏','安徽','福建','江西','山东'
    ,'河南','湖北','湖南','广东','广西','重庆','四川','贵州','西藏','陕西','甘肃','青海','宁夏','新疆','浙江']
#港澳台地区由于特殊，故不在爬取范围内。
#因为这批页面上浙江的网页缺乏2017年数据所以放到最后爬取
address0 = 'http://zhaoshengcx.nefu.edu.cn/f/zsjhAndLqfs/'#不同省份分数线的网站通用部分，后面加上省份就是对应网址。
address = ''
NefuList = list()#总列表
alist = ['College','Year','Province','Category','Major','Score','Contributor']#总列表的每一行
#依次是学校 年份 省份 文理 专业 最低分 作者名字
NefuList.append(copy.deepcopy(alist))#利用深复制防止意外发生，以下同理。
alist[0] = '东北林业大学'#这个是不变的
alist[6] = '09118213孙诚'#这个也是不变的
for Province in ProvinceList:
    address = address0 + Province#实际网址
    html = get(address)#获得相应html
    soup = BeautifulSoup(html, 'html.parser')#加工处理
    CGyyds = soup.find('tbody', {'class': 'tbody1'}).find_all('tr')#加工处理提取最小的包含所有分数的tag

    for i in CGyyds:
        tri = i.find_all('td')
        alist[2] = Province#省份
        alist[3] = tri[0].get_text()#文理
        alist[4] = tri[1].get_text()#专业

        alist[1] = '2019'
        alist[5] = StrNum(tri[5].get_text())#19年分数线，使用StrNum函数去除多余字符，以下同理。
        if alist[5]:#分数为空则表示当年未开设此专业，故不予记载。
            NefuList.append(copy.deepcopy(alist))

        alist[1] = '2018'
        alist[5] = StrNum(tri[7].get_text())#18年分数线
        if alist[5]:
            NefuList.append(copy.deepcopy(alist))

        if Province != '浙江':#很神奇唯独浙江的页面只有2019年和2018年分数线
            alist[1] = '2017'
            alist[5] = StrNum(tri[9].get_text())#17年分数线
            if alist[5]:
                NefuList.append(copy.deepcopy(alist))

    print(Province+' is over')#表示一个省份已经爬完

for i in NefuList:
    print(i)

#接下来把数据存入csv文件
with open("C:\\Users\Administrator\Desktop\CSV\\09118213孙诚_东北林业大学.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(NefuList)
