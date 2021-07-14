import requests
from bs4 import BeautifulSoup
import openpyxl


# 检查url地址
# 读取文本内容
def check_link(url,data):
    try:
        r = requests.post(url,data=data)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        return r.text
    except:
        print('无法链接服务器！！！')


# 爬取资源
# 通过标题获取年份和省份
def get_contents(rurl):
    ulist=[]
    soup = BeautifulSoup(rurl,'lxml')
    title = list(soup.find_all('h3'))  # 爬取标题（我这里是h3）
    title = str(title[0])  # 标题字符化
    # print(title)
    year = (title[9]+title[10]+title[11]+title[12])  # 获取年份
    province = (title[14]+title[15]+title[16])  # 获取省份
    # print('y',year)
    trs = soup.find_all('tr')  # 获取表格数据
    for tr in trs:
        ui = []
        ui.append(year)
        ui.append(province)  # 在每个列表里添加年份和省份
        for td in tr:
            if td != '\n':
                ui.append(td.get_text())  # 获取每一行表格数据
        if len(ui) != 2:  # 去除空列表项（新添了两项）（可能是换行）
            ulist.append(ui)
    return ulist


# 以csv存储数据
def csv_save(list,data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'College'
    sheet['B1'] = 'Year'
    sheet['C1'] = 'Province'
    sheet['D1'] = 'Category'
    sheet['E1'] = 'Major'
    sheet['F1'] = 'Score'
    sheet['G1'] = 'Contributor'
    contributor = '09118207朱斌'
    sheet.title = '吉林大学近三年录取分数线'
    college = '吉林大学'
    excel = []
    for inlist in list:
        excel.append([college, inlist[0], inlist[1], inlist[3], inlist[4], inlist[6], contributor])
    for excel_data in excel:
        sheet.append(excel_data)
    wb.save('09118207朱斌-吉林大学.csv')


# 处理函数封装
def process(url, data, urli):
    rs = check_link(url, data)
    ulist = get_contents(rs)
    # print('s', ulist)
    for i in ulist[1:len(ulist) - 1]:  # 去掉列表首个概阔与最后一个注释
        urli.append(i)


# 通过post和data爬取相同url的网站
def main():
    urli = []
    url = "http://zsb.jlu.edu.cn/Index/admission.html"
    data = []
    # 从现在开始，做一个无情的data寻找机器
    # 选择性舍去了一些地方省份的数据
    data1 = {'lnlqnf': '2019',
'lnlqsheng': 'jl',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data1)
    data2 = {'lnlqnf': '2019',
'lnlqsheng': 'bj',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data2)
    data3 = {'lnlqnf': '2019',
'lnlqsheng': 'tj',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data3)
    data4 = {'lnlqnf': '2019',
'lnlqsheng': 'heb',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data4)
    data5 = {'lnlqnf': '2019',
'lnlqsheng': 'sx',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data5)
    data6 = {'lnlqnf': '2019',
'lnlqsheng': 'ln',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data6)
    data7={'lnlqnf': '2019',
'lnlqsheng': 'sh',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data7)
    data8={'lnlqnf': '2019',
'lnlqsheng': 'js',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data8)
    data9={'lnlqnf': '2019',
'lnlqsheng': 'zj',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data9)
    data10={'lnlqnf': '2019',
'lnlqsheng': 'ah',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data10)
    data11 = {'lnlqnf': '2019',
'lnlqsheng': 'fj',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data11)
    data12={'lnlqnf': '2019',
'lnlqsheng': 'jx',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data12)
    data13={'lnlqnf': '2019',
'lnlqsheng': 'sd',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data13)
    data14={'lnlqnf': '2019',
'lnlqsheng': 'hen',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data14)
    data15={'lnlqnf': '2019',
'lnlqsheng': 'hub',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data15)
    data16={'lnlqnf': '2019',
'lnlqsheng': 'hun',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data16)
    data17={'lnlqnf': '2019',
'lnlqsheng': 'gd',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data17)
    data18={'lnlqnf': '2019',
'lnlqsheng': 'sc',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data18)
    data19={'lnlqnf': '2019',
'lnlqsheng': 'gz',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data19)
    data20={'lnlqnf': '2019',
'lnlqsheng': 'yn',
'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
'__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data20)
    data21 = {'lnlqnf': '2018',
             'lnlqsheng': 'jl',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data21)
    data22 = {'lnlqnf': '2018',
             'lnlqsheng': 'bj',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data22)
    data23 = {'lnlqnf': '2018',
             'lnlqsheng': 'tj',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data23)
    data24 = {'lnlqnf': '2018',
             'lnlqsheng': 'heb',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data24)
    data25 = {'lnlqnf': '2018',
             'lnlqsheng': 'sx',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data25)
    data26 = {'lnlqnf': '2018',
             'lnlqsheng': 'ln',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data26)
    data27 = {'lnlqnf': '2018',
             'lnlqsheng': 'sh',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data27)
    data28 = {'lnlqnf': '2018',
             'lnlqsheng': 'js',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data28)
    data29 = {'lnlqnf': '2018',
             'lnlqsheng': 'zj',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data29)
    data30 = {'lnlqnf': '2018',
              'lnlqsheng': 'ah',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data30)
    data31 = {'lnlqnf': '2018',
              'lnlqsheng': 'fj',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data31)
    data32 = {'lnlqnf': '2018',
              'lnlqsheng': 'jx',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data32)
    data33 = {'lnlqnf': '2018',
              'lnlqsheng': 'sd',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data33)
    data34 = {'lnlqnf': '2018',
              'lnlqsheng': 'hen',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data34)
    data35 = {'lnlqnf': '2018',
              'lnlqsheng': 'hub',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
                         '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data35)
    data36 = {'lnlqnf': '2018',
              'lnlqsheng': 'hun',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data36)
    data37 = {'lnlqnf': '2018',
              'lnlqsheng': 'gd',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data37)
    data38 = {'lnlqnf': '2018',
              'lnlqsheng': 'sc',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data38)
    data39 = {'lnlqnf': '2018',
              'lnlqsheng': 'gz',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data39)
    data40 = {'lnlqnf': '2018',
              'lnlqsheng': 'yn',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data40)
    data41 = {'lnlqnf': '2017',
             'lnlqsheng': 'jl',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data41)
    data42 = {'lnlqnf': '2017',
             'lnlqsheng': 'bj',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data42)
    data43 = {'lnlqnf': '2017',
             'lnlqsheng': 'tj',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data43)
    data44 = {'lnlqnf': '2017',
             'lnlqsheng': 'heb',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data44)
    data45 = {'lnlqnf': '2017',
             'lnlqsheng': 'sx',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data45)
    data46 = {'lnlqnf': '2017',
             'lnlqsheng': 'ln',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data46)
    data47 = {'lnlqnf': '2017',
             'lnlqsheng': 'sh',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data47)
    data48 = {'lnlqnf': '2017',
             'lnlqsheng': 'js',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data48)
    data49 = {'lnlqnf': '2017',
             'lnlqsheng': 'zj',
             'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
             '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data49)
    data50 = {'lnlqnf': '2017',
              'lnlqsheng': 'ah',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data50)
    data51 = {'lnlqnf': '2017',
              'lnlqsheng': 'fj',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data51)
    data52 = {'lnlqnf': '2017',
              'lnlqsheng': 'jx',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data52)
    data53 = {'lnlqnf': '2017',
              'lnlqsheng': 'sd',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data53)
    data54 = {'lnlqnf': '2017',
              'lnlqsheng': 'hen',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data54)
    data55 = {'lnlqnf': '2017',
              'lnlqsheng': 'hub',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
                         '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data55)
    data56 = {'lnlqnf': '2017',
              'lnlqsheng': 'hun',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data56)
    data57 = {'lnlqnf': '2017',
              'lnlqsheng': 'gd',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data57)
    data58 = {'lnlqnf': '2017',
              'lnlqsheng': 'sc',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data58)
    data59 = {'lnlqnf': '2017',
              'lnlqsheng': 'gz',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data59)
    data60 = {'lnlqnf': '2017',
              'lnlqsheng': 'yn',
              'entoken': 'wmt6mFZWrQ539/XQH4g28/72/NzfgwniGa9czVZ/4WwP',
              '__hash__': '6666cd76f96956469e7be39d750cc7d9_7086baaa9801b9d94d5c757750f76391'}
    data.append(data60)
    for i in data:
        process(url,i,urli)
    # print(urli)
    csv_save(urli, data)


main()