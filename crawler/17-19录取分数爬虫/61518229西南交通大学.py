# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:27:46 2020

@author: yjw
"""
import re #正则表达式进行文字的匹配
import urllib.request,urllib.error #获取网页的数据
import urllib
import xlwt #进行excle操作
book=xlwt.Workbook(encoding="utf-8")
sheet=book.add_sheet("sheet1",cell_overwrite_ok=True)
sheet.write(0,0,"college")
sheet.write(0,1,"Year")
sheet.write(0,2,"Province")
sheet.write(0,3,"Category")
sheet.write(0,4,"Major")
sheet.write(0,5,"Score")
sheet.write(0,6,"contributor")
c=1
def getdata(baseurl,year):#解析页面数据并且存入excel，其中baseurl为网页的url，year为查询的年份
    urllist=[]
    with open('各个省份的url.txt', 'r') as f:#将所有获得的URL放在一个txt文件里面
        a=[]
        for line in f:
            line=line.rstrip("\n")
            a.append(line)
    for txt in a:
        item=baseurl+str(year)+"/"+str(txt)
        urllist.append(item)
    sf=["四川","天津","上海","重庆","河北","山西","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","海南","北京","贵州","云南","陕西","甘肃","青海","内蒙古","广西","西藏","宁夏","新疆"]
    pat=re.compile("\"最低分\":\"\d+\"")
    pat1=re.compile("\"类别名称\":\".*?\"")
    pat2=re.compile(r'"专业名称":"(.*?)"')
    length=len(urllist)
    global c
    for j in range(0,length):
        i=1
        #sheet=book.add_sheet(sf[j],cell_overwrite_ok=True)#按照省份分为不同的sheet，没有数据的省份跳过
        url=urllist[j]+str(i)+"/10"
        while len(askurl(url))>30:
            html=askurl(url)
            s=re.findall(pat,html)
            s=re.findall("\d+",str(s))#分数
            y=re.findall(pat1,html)#文理科
            y=re.findall(r':"(.*?)"',str(y))
            t=re.findall(pat2,html)#专业
            for k in range(0,len(s)):#将数据写入excel，其中没有分数线的自动跳过
                sheet.write(c+(i-1)*len(s),0,"东南大学")
                sheet.write(c+(i-1)*len(s),1,year)
                sheet.write(c+(i-1)*len(s),2,sf[j])
                sheet.write(c+(i-1)*len(s),3,y[k])
                sheet.write(c+(i-1)*len(s),4,t[k])
                sheet.write(c+(i-1)*len(s),5,s[k])
                sheet.write(c+(i-1)*len(s),6,"61518229游家伟")
                c=c+1
            i=i+1   
            url=urllist[j]+str(i)+"/10"
def askurl(url):#获取页面数据
    head={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:#异常处理
        response=urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
    except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    return html 
def main():
    #主函数入口
    baseurl="https://zhaosheng.swjtu.edu.cn/select/excel/135/"
    getdata(baseurl,2017)
    getdata(baseurl,2018)
    getdata(baseurl,2019)
    book.save('西南交通大学2021年各省份分数线以及专业.xls')
if __name__=="__main__":
    main()