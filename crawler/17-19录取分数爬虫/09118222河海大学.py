from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#获取html文档
res2017 = urlopen("http://zsw.hhu.edu.cn/a/zhaoshengxinxi/linianqingkuang/20180403/601.html").read().decode('utf-8')
res2018 = urlopen("http://zsw.hhu.edu.cn/a/zhaoshengxinxi/linianqingkuang/20190515/684.html").read().decode('utf-8')
res2019 = urlopen("http://zsw.hhu.edu.cn/a/zhaoshengxinxi/zhaoshengkuaixun/2019/0810/744.html").read().decode('utf-8')
#若连接出错, 可替换为已经下载到本地的html测试 (file协议不支持相对路径, 需自指定路径)
# res2017 = urlopen("file:///d:/2017.html").read().decode('utf-8')
# res2018 = urlopen("file:///d:/2018.html").read().decode('utf-8')
# res2019 = urlopen("file:///d:/2019.html").read().decode('utf-8')


#2017,2018分数线都以一张表格的形式呈现
tab17 = BeautifulSoup(res2017, features='lxml').table
tab18 = BeautifulSoup(res2018, features='lxml').table
#2019本科一批的理工/文史分两张表
tab19 = BeautifulSoup(res2019, features='lxml').find_all("table",limit=2)
tab19a = tab19[0] #理工
tab19b = tab19[1] #文史

#省份列表
isProvince=["北","天","河","山","内","辽","吉","黑","上","浙","安","福","江","湖","广","海","西","重","四","贵","云","陕","甘","青","宁","新"]

#解析2017 (综合改革不计)
list2017=[]
rec17 = tab17.find_all("tr") #提取记录
for i in rec17: #筛选记录
    if i.td.string and i.td.string[0] in isProvince:
        #[省份, 理, 文]
        list2017.append([i.td.string, i.find_all("td")[2].string, i.find_all("td")[5].string])

#解析2018
list2018=[]
rec18 = tab18.find_all("tr") #提取记录
for i in rec18: #筛选记录
    if i.td.string and i.td.string[0] in isProvince:
        #[省份, 理, 文]
        list2018.append([i.td.string, i.find_all("td")[1].string, i.find_all("td")[3].string])

#解析2019 (综合改革不计)
list2019=[]
rec19a = tab19a.find_all("tr") #筛选理科
for i in rec19a:
    if i.td.string and i.td.string[0] in isProvince:
        if not i.td.string[0] == "上" and not i.td.string[0] == "西":
            list2019.append([i.td.string.replace("\xa0","").replace(" ",""), i.find_all("td")[2].string])
rec19b = tab19b.find_all("tr") #筛选文科
count = 0
for i in rec19b:
    if i.td.string and i.td.string[0] in isProvince:
        if not i.td.string[0] == "上" and not i.td.string[0] == "西":
            list2019[count].append(i.find_all("td")[2].string)
            count += 1


#输出文件
path = "09118222-沈毅_河海大学.csv"
with open(path,'w' ,newline='',encoding='utf-8-sig') as f:
    csv_write = csv.writer(f)
    csv_head = ["College","Year","Province","Category","Score"]
    csv_write.writerow(csv_head)
    #写数据
    for i in list2017:
        csv_write.writerow(["河海大学","2017",i[0],"理科",i[1]])
        csv_write.writerow(["河海大学","2017",i[0],"文科",i[2]])
    for i in list2018:
        csv_write.writerow(["河海大学","2018",i[0],"理科",i[1]])
        csv_write.writerow(["河海大学","2018",i[0],"文科",i[2]])
    for i in list2019:
        csv_write.writerow(["河海大学","2019",i[0],"理科",i[1]])
        csv_write.writerow(["河海大学","2019",i[0],"文科",i[2]])
