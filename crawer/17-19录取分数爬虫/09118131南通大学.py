from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
def link_process(url):  #对网址进行处理
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def content_process(ulist,rurl): #对页面内容进行处理
    soup = BeautifulSoup(rurl,'lxml')
    trs = soup.find_all('tr')   #读取表格的每一行
   # s=set()   #记录了数据类型
    for tr in trs:
        ui = []
        for td in tr:
            #s.add(type(td))#观察发现只有<class 'bs4.element.NavigableString'>, <class 'bs4.element.Tag'>两种数据类型
            if td.string==None: #对<class 'bs4.element.Tag'>直接取.string是空值
                #print(td.attrs)
                if 'x:num' in td.attrs:#对Tag的属性观察后发现键'x:num'对应的值是我们要的结果
                    ui.append(td['x:num'])
            else:
                ui.append(td.string)
        ulist.append(ui)
    #print(s)

def processJS(url,year):  #对江苏的招生信息进行处理
    urli = []
    rs = link_process(url)
    content_process(urli,rs)
    for i in urli:       #去除列表中的空格元素，便于下面的操作
        for _ in i:
            if ' ' in i:
                i.remove(' ')
    index=urli.index(['本科一批'])
    for i in range(index+2):#将提前批等非本一批删除
        urli.pop(0)
    index1=urli.index(['序号', '科类', '专业名称', '招生数', '最高分', '最低分', '平均分'])
#在对提取后的数据进行分析时发现，后面的会计学、建筑学等一些中外合办的专业不属于本科一批普通类（专业最低分比学校提供的本一投档线低）
#然而对相关专业批次的说明2019的网页中未曾标出，在2018的网页中才有明确的注释
#使得确定本一批次范围的下界有一定的困难，所以使用了index1中的元组作为下界标识
    name=['College','Year','Province','Category','Major','Score','Contributor']#列名
    Category=[]
    Major=[]
    Score=[]
    for i in urli[:index1]:
        if len(i)==7:  #去除其他长度的列表的影响
            if i[1]=='文科':
                Category.append('文科')
                Major.append(i[2])   #专业
                Score.append(i[5])   #最低分
            elif i[1]=='理科':
                Category.append('理科')
                Major.append(i[2])   #专业
                Score.append(i[5])   #最低分
            else:
                continue
    lenth=len(Category)
    College=['南通大学' for _ in range(lenth)]  #学校名
    Year=[year for _ in range(lenth)]    #年份
    Province=['江苏' for _ in range(lenth)]   #省份
    Contributor=['09118131唐云龙' for _ in range(lenth)]
    array=np.array([College,Year,Province,Category,Major,Score,Contributor])
    array=array.transpose()
    result=pd.DataFrame(array,columns=name)
    #print(result)
    return result

def judge(record):#用来判断属于哪个Category
    L=['本一理科','本科批理科','本科A批理科','本科理科']
    w=['本一文科','本科批文科','本科A批文科','本科文科']
    A=['本科批A段','本科批','普通本科批']
    JudgeClass=[]              #这里采用了取交集判断类别的方法
    judge1=list(set(L)&set(record))
    judge2=list(set(w)&set(record))
    judge3=list(set(A)&set(record))
    JudgeClass.append(judge1)
    JudgeClass.append(judge2)
    JudgeClass.append(judge3)
    return JudgeClass

def processOther(url,year):#其他各省与江苏省的格式不同，另建一个函数进行处理
    urli = []
    rs = link_process(url)
    content_process(urli,rs)
    for i in urli:          #去空格
        for _ in i:
            if ' ' in i:
                i.remove(' ')
    #print(urli)
    name=['College','Year','Province','Category','Major','Score','Contributor']
    Province=[]
    Category=[]
    Score=[]
    for i in urli[1:]: #避免第一条列表中列名的影响
        if len(i)==8:  #因存在一个省份单元格对应多行记录的情况,读出的列表长短不一。长度为8的列表中才包含省份
            pro=i[1]     #保存省份值，以便添加
        judgement=judge(i)  #判断类别，judgement每个元素都是一个列表
        if judgement[0]:
            Category.append('理科')
        elif judgement[1]:
            Category.append('文科')
        elif judgement[2]:
            Category.append(' ')
        else:
            continue   #本二或其他
        if len(i)==8:   #长度不同的列表最低分下标不同，分开处理
            Province.append(pro)
            Score.append(i[6])
        else:
            Province.append(pro)
            Score.append(i[4])
        
        
    lenth=len(Score)
    College=['南通大学' for _ in range(lenth)]   #学校
    Year=[year for _ in range(lenth)]         #年份
    Contributor=['09118131唐云龙' for _ in range(lenth)]
    Major=['all' for _ in range(lenth)]        #专业
    array=np.array([College,Year,Province,Category,Major,Score,Contributor])
    array=array.transpose()
    result=pd.DataFrame(array,columns=name)
    #print(result)
    return result

url1='http://zs.ntu.edu.cn/2020/0214/c5209a137264/page.htm'
year='2019'
result1=processJS(url1,year)

url2='http://zs.ntu.edu.cn/2019/1216/c5209a137262/page.htm'
year='2019'
result2=processOther(url2,year)


url3='http://zs.ntu.edu.cn/2018/1115/c5209a137261/page.htm'
year='2018'
result3=processJS(url3,year)


url4='http://zs.ntu.edu.cn/2018/1115/c5209a137259/page.htm'
year='2018'
result4=processOther(url4,year)

result=pd.concat([result1,result2,result3,result4], axis=0)#连接合并
print(result)
result.to_csv('D:/Result.csv',encoding = 'utf-8-sig',index=False)
