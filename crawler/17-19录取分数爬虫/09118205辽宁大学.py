import requests
from bs4 import BeautifulSoup
import bs4
import csv

def getHTMLText(url): #对页面进行request的方法
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")
        return ""


def ScoreList(ulist, html):#获取网页的html文件并进行分析，通过table的ID进行定位，得到表格中我们需要爬取的相应信息
    soup = BeautifulSoup(html, "html.parser")
    table=soup.find_all(class_='cls-data-table')[1]
    trs=table.find_all('tr')
    for tr in trs:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[1].string, tds[2].string, tds[3].string,tds[4].string,tds[10].string])
    pass


def main():#定义主函数
    ufo = []#存储信息的列表
    h_url = "http://zsxt.lnu.edu.cn/zsb/ShowReport.wx?DISPLAY_TYPE=1&PAGEID=zsb_xs_lqfs_query&nf=&sf=&zy=&report1_PAGECOUNT=17&report1_RECORDCOUNT=3350&report1_PAGENO="
    #通过分析网页url 发现不同页面的url在网页链接处没有变化 认为有隐藏参数 于是在xhr中找到真正的url，其中只有最后的PAGENO参数有变化，代表着表格的显示页数
    for i in range(17):#爬取P1-P17所有页面的所需内容
        url=h_url+str(i+1)
        html = getHTMLText(url)
        ScoreList(ufo, html)
        print(i+1," of 17 is done")#展示爬取进程

    #将信息保存为csv文件
    header=["College","Year","Province","Category","Major","Score","Contributor"]#第一行为表头
    a=["辽宁大学"]
    b=["09118205王昕彤"]
    with open('09118205王昕彤-辽宁大学.csv', 'w', newline='')as f:#打开文件
        fw=csv.writer(f)#写入文件
        fw.writerow(header)
        for i in range(len(ufo)):
            if ufo[i][0] == "2015":#筛掉2015年的数据
                break
            if ufo[i][4]=="0" or ufo[i][4]=='':#筛掉最低分数线处为0或无成绩的数据
                continue
            c=a+ufo[i]+b
            fw.writerow(c)
    f.close()

#run
main()

