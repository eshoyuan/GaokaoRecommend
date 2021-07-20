import requests
from bs4 import BeautifulSoup
import openpyxl
import re
from urllib.request import urlopen
#对网页进行处理
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)#获取url信息
        r.raise_for_status()#异常信息
        r.encoding = 'utf-8'
        return r.text#返回该链接的网页信息
    except:
        return "error"
#获取网页中的相关录取信息   
def getList(soup,url):
    list=[]#信息数据集
    #获取title中的年份信息
    content = urlopen(url).read().decode('utf-8')
    pat = r'<title>(.*?)</title>'
    title = re.findall(pat,content)
    year=str(title[0][0:4])
    #获取网页中表格内的各部分信息
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        singleUniv.append(year)
        for td in ltd:
            singleUniv.append(td.string)
        list.append(singleUniv)
    return list
#对信息列表进行预处理，将文理科分数相同的省份补充完整
def processList(list):
    for u in list:
        if len(u)==4:
            temp=u[3]
            u[3]=u[2]
            u.append(temp)
    return list
#将信息列表的信息写入csv文件中
def csv_save(list):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'year'
    sheet['B1'] = 'province'
    sheet['C1'] = 'category'
    sheet['D1'] = 'score'
    sheet['E1'] = 'major'
    sheet['F1'] = 'contributor'
    major='all'
    contributor='09118227张文杰'
    sheet.title = '浙江大学录取线'
    data_excel = []
    for inlist in list:
        for u in inlist[1:]:
            data_excel.append([u[0],u[1],inlist[0][2], u[2],major,contributor])
            data_excel.append([u[0],u[1],inlist[0][3], u[3],major,contributor])
            data_excel.append([u[0],u[1],inlist[0][4], u[4],major,contributor])
    for data in data_excel:
        sheet.append(data)
    wb.save('09118227张文杰-浙江大学.csv')
#将函数分装到一起，构成爬虫函数      
def crawlerfunction(url):
    inforList=[]
    for inurl in url:
        html= getHTMLText(inurl)
        soup= BeautifulSoup(html, "html.parser")
        inforListi=getList(soup,inurl)
        inforListi=processList(inforListi)
        inforList.append(list(inforListi))
    csv_save(inforList)

def main():
    url1='https://zdzsc.zju.edu.cn/2019/1025/c3303a1728176/page.htm'
    url2='https://zdzsc.zju.edu.cn/2019/0514/c3303a1197450/page.htm'
    crawlerfunction([url1,url2])

main()