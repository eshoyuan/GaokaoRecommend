import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv

def html_get(url):
    ua = UserAgent(use_cache_server=False)
    ua.random
    headers={'User-Agent': 'ua'}

    response = requests.post(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

def html_post(url,data):
    ua = UserAgent(use_cache_server=False)
    ua.random

    headers={'User-Agent': 'ua'}

    response = requests.post(url, data=data, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

# 获取省份信息
html = html_get('http://zsbwx.neau.edu.cn/web-pc/lncj.jsp')
soup = BeautifulSoup(html,'html.parser')
infos = soup.find('td',{'width':'12%','align':'left'}).find_all('option')
sf = []
for i in infos:
    sf.append(i.get_text())

# 获取每个省份的科类和批次
url = 'http://zsbwx.neau.edu.cn/web-pc/lncj.jsp?types=pckl&cx_sf='
pc = []
kl = []

for i in range(len(sf)):
    kl.append([])
    pc.append([])

k = 0
for i in sf:
    new_url = url + i
    html = html_get(new_url)
    soup = BeautifulSoup(html, 'html.parser')
    kls = soup.find('select', {'name': 'cx_kl', 'id': 'selectyx'}).find_all('option')
    pcs = soup.find('select', {'name': 'cx_pc', 'id': 'selectzy'}).find_all('option')

    for j in kls:
        kl[k].append(j.get_text())
    for l in pcs:
        pc[k].append(l.get_text())
    k += 1

for i in range(len(kl)):
    if '请选择' in kl[i]:
        kl[i].remove('请选择')
    if '请选择' in pc[i]:
        pc[i].remove('请选择')

# 通过省份、科类和批次信息构造表单
data = []
year = [2019, 2018, 2017]

for i in range(len(year)):
    for j in range(len(sf)):
        for k in range(len(kl[j])):
            for l in range(len(pc[j])):
                data.append({'cx_nf':year[i], 'cx_sf':sf[j], 'cx_kl':kl[j][k], 'cx_pc':pc[j][l], 'Button1':'查询'})

# 获取历年分数
information = []
a = []

for i in data:
    html = html_post('http://zsbwx.neau.edu.cn/web-pc/lncj.jsp',data=i)
    soup = BeautifulSoup(html,'html.parser')
    infos = soup.find('table',{'width':'950','border':'0','cellspacing':'1'}).find_all('tr')                        

    for i in infos:
        info = i.find_all('td')
        for j in info:
            a.append(j.get_text())
        information.append(a)
        a = []


# 处理数据
r = ['年份', '省份', '批次', '科类', '专业', '学制',
    '录取数', '省控线', '最高分', '最低分', '平均分',
    '最低分\r\n                    全省名次', '备注']

while r in information:
    information.remove(r)

my_info = [['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor']]
for i in information:
    my_info.append(['东北农业大学', i[0], i[1], i[3], i[4], i[9], '09118212陈耿'])

# 保存数据
with open("09118212陈耿-东北农业大学.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(my_info)