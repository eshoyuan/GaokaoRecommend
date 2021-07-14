import requests
from bs4 import BeautifulSoup
import time
import csv

"""获取HTML页面"""
def getHTMLText(url,param = None,kv = None,code = 'utf-8'):
     try:
        r = requests.post(url,params = param, data = kv)
        r.raise_for_status()
        r.encoding = code
        return r.text
     except:
        return ""
    
"""获取信息"""
def getInfoList(slist,url,param,kv):
    html = getHTMLText(url,param,kv)
    if html == "":
        return
    soup = BeautifulSoup(html,'html.parser')
    tr = soup.find_all('tr')
    for i in tr:
        lst1 = []
        for td in i.find_all('td'):
            lst1.append(td.string)
        if lst1 not in slist:
            slist.append(lst1)             

'''起始信息'''          
year = ['2018','2019']#缺少2017年信息
place = ['安徽', '北京', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '河南', 
         '黑龙江', '湖北', '湖南', '吉林', '江苏', '江西', '辽宁', '宁夏', '青海', '山东',
         '山西', '陕西', '上海', '四川', '天津', '西藏', '新疆', '云南', '浙江', '重庆']
param = {'g': 'apply','m': 'index','a': 'admit'}
url = "http://zsxt.ccnu.edu.cn/apply/index.php?g=apply&m=index&a=index"
lst = [{x:y} for x in year for y in place] #生成查询参数
slist = []#存储录取信息

'''循环调用getInfoList函数获得目标信息'''
count = 1 #记录进度
time1 =time.time()
for kv in lst:
    getInfoList(slist,url,param,kv)
    time2 = time.time() - time1 #用时
    print('\r当前进度：{:.2f}%\t用时：{:.2f}秒'.format((count * 100 /len(lst)),time2),end ='')
    count=count+1

'''处理数据'''     
for i in range(len(slist[0])-1,-1,-1):#倒序修改
    if slist[0][i] == '年份':
        slist[0][i] = 'Year'
    elif slist[0][i] == '省份':
        slist[0][i] = 'Province'
    elif slist[0][i] == '科类':
        slist[0][i] = 'Category' 
    elif slist[0][i] == '专业':
        slist[0][i] = 'Major'
    elif slist[0][i] == '最低分':
        slist[0][i] = 'Score'  
    elif slist[0][i] in [ '批次','最高分', '平均分']:
        for x in slist:
            x.remove(x[i])
    elif slist[0][i] == '备注':
        slist[0][i] = 'Contributor'
        for j in slist[1:]:
            j[i] = '09118242张骥'
            
for i in range(len(slist)):
    if i == 0:
        slist[i].insert(0,'College')
    else :
        slist[i].insert(0,'华中师范大学')
        
for i in range(len(slist)):
    for j in range(len(slist[i])):
        if slist[i][j] == '综合改革':
            slist[i][j] = 'all'
        
'''存储csv文件'''
f = open("D:\\华中师范.csv",'w',newline = '')
f.truncate()
csv_writer = csv.writer(f,dialect = 'excel')

for i in slist:
    csv_writer.writerow(i)

f.close()