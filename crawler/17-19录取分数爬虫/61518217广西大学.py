from bs4 import BeautifulSoup
from urllib import request
import datetime
import pandas as pd

#首先获取当前时间，确定需要获得的表的时间
#由此确定获取数据的范围
timenow=datetime.datetime.now().year
year=str(timenow)
#print(timenow)#timenow是数字，year是字符串
pointer=0 #pointer=1表示今年的统计表已经出来了，否则为0

# 要请求的网络地址，为广西大学招生信息的入口，下面有去往统计表的链接
url = 'http://zs.gxu.edu.cn/List.asp?L-8357204727.Html'
html = request.urlopen(url)#获取网页代码
soup = BeautifulSoup(html, 'html.parser')#整理代码
data = soup.find_all('a')#由于超链接都有的‘a’标签，获取它们


# 遍历所有的 a 标签， 获取它们的 href 属性的值和它们的 text，herf即为链接
textlist=[]
linklist=[]#用于存储文字和链接
front='http://zs.gxu.edu.cn'#获取的herf链接为相对链接，需要再加上前缀才是完整链接

for item in data:
    if item.string is not None and item['href'] != 'javascript:;' and item['href'] != '#':
        web=front+item.get('href')
        text=item.string
        if (('录取' in text) and ('表' in text)and ('艺术' not in text) and  ('少数' not in text)):#表、录取是关键词，暂时不考虑对艺术类和少数民族专业的获取
            textlist.append(text)
            linklist.append(web)
            if(year in text):
                pointer=1

#接下来筛选目标网站，按年份找出三个链接
textlist2=[]
linklist2=[]
yearlist=[]

for i,item in enumerate(linklist):
    str1=str(timenow+pointer-1)
    str2=str(timenow+pointer-2)
    str3=str(timenow+pointer-3)#利用pointer得到年份
    if(i==0):
        yearlist.append(str1)
        yearlist.append(str2)
        yearlist.append(str3)
    if(str1 in textlist[i]):
        textlist2.append(textlist[i])
        linklist2.append(item)
    if(str2 in textlist[i]):
        textlist2.append(textlist[i])
        linklist2.append(item)
    if(str3 in textlist[i]):
        textlist2.append(textlist[i])
        linklist2.append(item)

insideTEXTlist=[]
insideLINKlist=[]
outsideTEXTlist=[]
outsideLINKlist=[]
for i,item1 in enumerate(textlist2):
    if('区内' in item1):
        insideTEXTlist.append(item1)
        insideLINKlist.append(linklist2[i])
    else:
        outsideTEXTlist.append(item1)
        outsideLINKlist.append(linklist2[i])

#print(insideTEXTlist)
#print(insideLINKlist)
#print(outsideTEXTlist)
#print(outsideLINKlist)


#接下来从网站上爬取统计表中的内容
College=[]
Year=[]
Province=[]
Category=[]
Major=[]
Score=[]
Contributor=[]
strCollege='广西大学'
strContributor='61518217高奕辰'#首先准备好空列表


#由于广西大学的表分省内和省外的，所以先试着分两种进行爬取
#省内有具体专业，但省外的没有具体专业
#首先爬取省内的，省内的表比较规整，
for i,item in enumerate(insideLINKlist):
    alist = []
    blist = []
    tlist = []
    url1 = insideLINKlist[i]
    html1 = request.urlopen(url1)  # 获取网页代码
    soup1 = BeautifulSoup(html1, 'lxml')  # 整理代码
    trs = soup1.find_all('tr')  # 找到tr，为列表的行
    for tr in trs:
        tlist.append(tr)
    for item in tlist:
        spans = item.find_all('span')
        littlelist = []
        for span in spans:
            if(span.string==None):
                spanbig=span.find_all('span')
                span1=str(spanbig[0].previous_element)+'('+str(spanbig[1].previous_element)+')'
                littlelist.append(span1)#其中有一个中美合作的专业涉及两个span，进行特殊处理
            else:
                littlelist.append(span.string)
        alist.append(littlelist)
    #print(alist)
    for items in alist:
        for items2 in items:
            if(items2.__len__()<2):
                items.remove(items2)
        for items2 in items:
            if (items2.__len__() < 2):
                items.remove(items2)
                #span套span的项会多出俩个括号和一个逗号，要删去,但是不知道为什么删一次删不完全

    # 获得每行表，现在需要按内容获得序号
    indexMajor = 0
    indexCategory = 0
    indexLowScore = 0
    for items in alist[0]:
        if ('专业' in items and '类' not in items):
            indexMajor = alist[0].index(items)
        if ('科类' in items):
            indexCategory = alist[0].index(items)
        if ('最低分' in items):
            indexLowScore = alist[0].index(items)

    for items in alist[1::]:
        College.append(strCollege)
        Year.append(yearlist[i])
        Province.append('广西')
        Category.append(items[indexCategory])
        Major.append(items[indexMajor])
        Score.append(items[indexLowScore])
        Contributor.append(strContributor)

for i,item in enumerate(outsideLINKlist):
    alist = []
    blist = []
    tlist = []
    url1 = outsideLINKlist[i]
    html1 = request.urlopen(url1)  # 获取网页代码
    soup1 = BeautifulSoup(html1, 'lxml')  # 整理代码
    trs = soup1.find_all('tr')  # 找到tr，为列表的行
    for tr in trs:
        tlist.append(tr)
    for item in tlist:
        spans = item.find_all('span')
        littlelist = []
        for span in spans:
            if (span.string == None):
                spanbig = span.find_all('span')
                span1 = str(spanbig[0].previous_element) + '(' + str(spanbig[1].previous_element) + ')'
                littlelist.append(span1)  # 其中有一个中美合作的专业涉及两个span，进行特殊处理
            else:
                littlelist.append(span.string)
        alist.append(littlelist)
        # 省外的表有两种，需要分开进行处理（为啥不能年年一样？！，三年三种，我的能力只能每种都分开

    kind = 0  # 0代表2019年的表，1代表20182017的表
    for items in alist[0]:
        if ('科类' in items):
            kind = 1
    if (kind == 1):
        indexProvince = []
        indexCategory = []
        indexLowScore = []
        lengthOFa = alist[0].__len__()
        for i1 in range(0, lengthOFa):
            if ('科类' in alist[0][i1]):
                indexCategory.append(i1)
            if ('最低分' in alist[0][i1]):
                indexLowScore.append(i1)
            if ('省份' in alist[0][i1]):
                indexProvince.append(i1)

        for items in alist:
            for i2, item in enumerate(items):
                if (('文' == item) or ('理' == item)):
                    h = items[i2 - 1].isdigit()
                    if (items.index(item) == 0):
                        index1 = alist.index(items)
                        index2 = i2
                        element = alist[index1 - 1][index2]
                        items.insert(index2, element)
                    if ((i2 > 2) and (items[i2 - 1].isdigit())):
                        index1 = alist.index(items)
                        index2 = i2
                        element = alist[index1 - 1][index2]
                        items.insert(index2, element)

        # 上面把整张表补全为完全体
        for items in alist:
            while (True):
                if ('　' in items):
                    items.remove('　')
                if (',' in items):
                    items.remove(',')
                if (('　' not in items) and (',' not in items)):
                    break
        for i3, item in enumerate(items):
            if ('注' in item):
                items.remove(item)
        for items in alist:
            if (items.__len__() < 4):
                alist.remove(items)

        for n in (0, 1):
            for items in alist[1::]:
                if (items.__len__() > 8):
                    College.append(strCollege)
                    Year.append(yearlist[i])
                    Province.append(items[indexProvince[n]])
                    Category.append(items[indexCategory[n]])
                    Major.append('All')
                    Score.append(items[indexLowScore[n]])
                    Contributor.append(strContributor)
                else:
                    if (items.__len__() > 6):
                        College.append(strCollege)
                        Year.append(yearlist[i])
                        Province.append(items[indexProvince[0]])
                        Category.append(items[indexCategory[0]])
                        Major.append('All')
                        Score.append(items[indexLowScore[0]])
                        Contributor.append(strContributor)


    if (kind == 0):
        indexLowScore = []
        category2019=[]
        lengthOFa = alist[1].__len__()
        for i4 in range(0, lengthOFa):
            if ('最低分' in alist[1][i4]):
                indexLowScore.append(i4+1)
        category2019.append('理工')
        category2019.append('文史')

        for items in alist:
            while (True):
                if ('　' in items):
                    items.remove('　')
                if (',' in items):
                    items.remove(',')
                if (('　' not in items) and (',' not in items)):
                    break
        for i5, item in enumerate(items):
            if ('注' in item):
                items.remove(item)
        for items in alist:
            if (items.__len__() < 4):
                alist.remove(items)

        for items in alist[2::]:
            if ((items.__len__() > 8) and (items[0].__len__() == 2)):
                College.append(strCollege)
                Year.append(yearlist[i])
                Province.append(items[0])
                Category.append(category2019[0])
                Major.append('All')
                Score.append(items[indexLowScore[0]])
                Contributor.append(strContributor)

                College.append(strCollege)
                Year.append(yearlist[i])
                Province.append(items[0])
                Category.append(category2019[1])
                Major.append('All')
                Score.append(items[indexLowScore[1]])
                Contributor.append(strContributor)
            else:
                if ((items.__len__() > 8) and (items[0].__len__() == 3)):
                    College.append(strCollege)
                    Year.append(yearlist[i])
                    Province.append(alist[alist.index(items) - 1][0])
                    Category.append(category2019[0])
                    Major.append('高收费')  # 高收费的专业嘛，网站上是注释
                    Score.append(items[indexLowScore[0] - 1])
                    Contributor.append(strContributor)

                    College.append(strCollege)
                    Year.append(yearlist[i])
                    Province.append(alist[alist.index(items) - 1][0])
                    Category.append(category2019[1])
                    Major.append('高收费')  # 高收费的专业嘛，网站上是注释
                    Score.append(items[indexLowScore[1] - 1])
                    Contributor.append(strContributor)
            if (items.__len__() < 6):
                College.append(strCollege)
                Year.append(yearlist[i])
                Province.append(items[0])
                Category.append(category2019[0])
                Major.append('All')
                Score.append(items[indexLowScore[0]])
                Contributor.append(strContributor)

#最后把各个列表存为csv！
Name=['College','Year','Province','Category','Major','Score','Contributor']
DATA=[College,Year,Province,Category,Major,Score,Contributor]
Mylist=pd.DataFrame({'College':College,'Year':Year,'Province':Province,'Category':Category,'Major':Major,'Score':Score,'Contributor':Contributor})
Mylist.to_csv('61518217高奕辰-广西大学.csv',index=False,columns=Name)












