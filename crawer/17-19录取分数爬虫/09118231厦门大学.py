# 09118231 陈文丽
# 爬虫获取厦门大学2017-2019年本科生分数线
# 厦门大学往年录取网页链接：https://zs.xmu.edu.cn/5818/list.htm，该页面有2015-2019年本科录取情况和艺术生录取情况的链接
#本程序代码通过爬虫此页面获取2017-2019年本科录取情况的链接，然后在进一步对所获取的链接进行爬虫，从而获得每一个年份的信息

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://zs.xmu.edu.cn/5818/list.htm' #厦门大学往年录取网页


#通过爬虫获取2017-2019年的本科生录取情况的网页链接
strhtml1 = requests.get(url)
strhtml1.encoding='utf-8'#为了顺利显示中文
soup=BeautifulSoup(strhtml1.text,'lxml')
#选择所需的标签
dataUrls =  soup.select('#wp_news_w8 > div > div.col-lg-10.col-md-10.col-sm-9.col-xs-10.list-news-title > a')

#清洗数据，留下需要的网页链接
urlsNormal=[]#存储本科生的录取情况相关页面的链接
i=0#计数，2017-2019年的链接在前六个，其中包括艺术生和本科生的录取情况
print("爬虫进展：")
for item in dataUrls:
    result=[item.get_text(),"https://zs.xmu.edu.cn"+item.get('href')]
    if "艺术" not in result[0]:
        urlsNormal.append(result)#留下本科生的链接
    i+=1
    if i>=6:
        break#只获取前六个即为2017-2019年本科生录取情况的链接
    #just get the information from 2017 to 2019. And for this website, each year has 2 links
print("获得的网页链接：",urlsNormal)#显示所爬取内容



#分别对上一步所获取的链接进行爬虫，从而获得详细信息，并将信息存入csv文件中

cleanData=pd.DataFrame()#用于存取所有经过初步清洗后的数据

Year=[2019,2018,2017]#年份列表
Contributor="09118231陈文丽"#Contributor的信息

y=0#计数，以显示年份
for i in urlsNormal:
    year=Year[y] #获取年份
    print(year)  # 显示进度
    y+=1

    urli=i[1]#当前所爬取网页的链接
    #通过对当前页面进行爬虫获取详细的表格信息
    strhtml2=requests.get(urli)
    strhtml2.encoding = 'utf-8'  # 为了顺利地显示中文信息
    soup = BeautifulSoup(strhtml2.text, 'lxml')
    trs = soup.find_all('tr')#获取tr标签的内容

    data = []  # 用于存取当年页面获取的信息
    #遍历表格依次获取每一行的数据
    for tr in trs:
        row = []#用于保存表格中每一行的数据

        #遍历每一行，获取行内每一个td标签内的数据
        for td in tr:

            #在每一个省份表格的第一个省份存储在span中，需要特殊处理
            if td.string==None:
                if td.span!= None:
                    row.append(td.span.get_text())
            else:
                row.append(td.string)
        row.append(year)#添加年份信息
        row.append(Contributor)#添加Contributor的信息

        data.append(row)#将获取的每一行信息添加信息中
    data = pd.DataFrame(data)#转换为DataFrame，以便于后期处理数据

    #初步清洗当前年份的数据
    delIndex = []#用于存取需要删除的行的信息

    #通过遍历，删除所有没有具体录取专业的信息（表头不含有"录取专业"）以及每一个省份的表头（表头中含有"录取专业"）
    for i in range(data.shape[0]):
        if "录取专业" in data.iloc[i].tolist():
            delIndex.append(i)
           # data.iloc[i,[9,10]]=["Year","Contributor"]
            for j in range(i+1,data.shape[0]):
                if "录取专业" in data.iloc[j].tolist():
                    delIndex.append(j)#记录每一个省份的表头所在的行索引
            break
        else:
            delIndex.append(i)#记录没有具体录取专业的信息所在的行索引
    data = data.drop(delIndex)#删除所以记录的行

    cleanData=cleanData.append(data,ignore_index=True)#将初步清洗后的当前年份的数据记录下来

#进一步清洗数据，获取最终所要的数据
cleanData=cleanData.drop(range(10,cleanData.shape[1]),axis=1)#将数据表格多余的空列删掉
cleanData.columns=['Province','录取类别','Category','Major','录取最高分','录取平均分','Score','录取人数','Year','Contributor']#设定表头方便进行数据选择
finalResult=pd.DataFrame({"College":["厦门大学"]*cleanData.shape[0]})#在最终结果中记录College信息
finalResult=pd.concat([finalResult,cleanData[['Year','Province','Category','Major','Score','Contributor']]],axis=1)#将所需要的信息添加到最终结果中

#将所获得的数据存储在文件中
finalResult.to_csv("09118231陈文丽-厦门大学.csv",header=True, index=False,encoding='utf_8_sig')


