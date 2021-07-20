import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import random
import json
import pandas as pd


# 获取下拉框中的选项
province = []
year = []
category = []
genre = []
bacth = []
choices = [province, year, category, genre, bacth]

url = 'http://zsb.bjfu.edu.cn/f/cjcx'
strhtml = requests.get(url)  # Get方式获取网页数据
soup=BeautifulSoup(strhtml.text,'lxml')
print(soup.title)

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('http://zsb.bjfu.edu.cn/f/cjcx')
html = driver.page_source
selects = BeautifulSoup(html, 'lxml').find_all(class_='comp_select select1')
i = -1
for select in selects:
    i += 1
    all_li = select.find_all('li')
    for li in all_li:
        choices[i].append(li.text)
print(choices)


# User-Agent列表，用于伪装浏览器的User Agent
USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
]


# 设置cookie
Cookie = "zsb.bjfu.session.id=707a7e6aa6244911832d1b4137a95f26"
# 设置动态js的url
url = 'http://zsb.bjfu.edu.cn/f/lnzyzsjhcjcx'
# 设置requests请求的 headers
headers = {
    'User-agent': random.choice(USER_AGENTS),  # 设置get请求的User-Agent，用于伪装浏览器UA
    'Cookie': Cookie,
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'zsb.bjfu.edu.cn',
    'Referer': 'http://zsb.bjfu.edu.cn/f/cjcx'
}

datas=[]
for y in year:
    for p in province:
        for c in category:
            for g in genre:
                for b in bacth:
                    data={'nf': y,
                          'ssmc': p,
                          'klmc': c,
                          'zylx': g,
                          'zycc': b
                          }
                    datas.append(data)

result = []
for data in datas:
    # requests post请求
    req = requests.post(url, data=data, headers=headers)
    # 获取包含json数据的字符串
    str_data = req.content
    # 把json数据转成dict类型
    json_Info = json.loads(str_data)
    for dic in json_Info["sszygradeLnZyList"]:
        record=['北京林业大学',dic['nf'],dic['ssmc'],dic['klmc'],dic['zymc'],dic['minScore'],'09118112张硕']
        result.append(record)


df = pd.DataFrame(result, columns=['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])
path='09118112_张硕_北京林业大学.csv'
df.to_csv(path,index=False,header=True,encoding='gbk')