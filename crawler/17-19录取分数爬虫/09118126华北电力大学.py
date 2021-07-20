# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:02:20 2020

@author: Dingz
"""

import requests
from bs4 import BeautifulSoup
import csv

file_path = r'C:\\Users\\Dingz\\Desktop\\09118126丁自超-华北电力大学.csv'
file = open(file_path,"w",encoding="utf-8",newline='')
csv_writer = csv.writer(file)
#构建表头
csv_writer.writerow(["College","Year","Province","Category","Major","Score","Contributor"])

urls=['https://goto.ncepu.edu.cn/bkzn/wnfs/c546b0aad1024a1bbb73f8b93b9b3540.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/8bd389ff3a734bbc9fabb478ef640eb0.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/a86655e18c9e42c9961b86be34c0c5ac.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/d9378c62413b433d9a43b70f24399c2b.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/12d1b3039b3c4e0baeff9dba433e8999.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/6060a27136e6465590eb4308ec04e87d.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/2e5a3a8a85ad4ddd9f3386a40892c8ab.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/7b871c8a18f047c4844122dc6f6d3442.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/ee6bfefd291643adbc5b3b48262dd60e.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/31c3ff45ff454948b9a693b265f7691c.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/edb2335d8e764dc1aa428ff75fc209c7.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/184fc33c75d94569a7f2cd83179f291a.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/83265792d99c4d8c895ab057db3e2367.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/8503c9ac9bc944c492f065f2f59541d7.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/8e91379ad57548f1a98b065224046362.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/b5828444be8f44c1bdf2541238b41c8f.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/4367efb3181e4fc88b996c3334e5d11f.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/36bd952cc03141f6863e90c38868bd36.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/aac5f227036244cb901df0634cabe874.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/3ff1ec56f75d40e4b8df542cc146f9fb.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/71225135f62c41729adaed2c26fe11ad.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/707586d6264b4fa29febda4fcb34d5dd.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/27007f2cbbcf4a3b8310f83c3e380a1d.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/ed928b7901b04c998554f2eed1b6a401.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/1e7937ae22d6422d8de79ec4087c9139.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/48164b8b0cda4c6cb0fbea5154039935.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/96ce9e501f974a1d8b4d573b65d27b03.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/50bbe988a33f43f5a913e99609037120.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/cccf44100ca44bda867fa22148306686.htm',
      'https://goto.ncepu.edu.cn/bkzn/wnfs/4569192c01a041c5a0546d75f2e2c142.htm']    #各省份往年分数网页

#解析网页
def get_html(url):
    headers = {
    'Connection': 'close','User-Agent': 'User-Agent:Mozilla/5.0'
    }
    page = requests.get(url, headers=headers,verify=False)
    return page.content

def analyse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    article = soup.find('div',attrs = {'class':'article'})
    title = soup.find('div',attrs = {'class':'articleTitle02'})
    text=title.get_text()
    #获取省份
    if len(text)>20:
        Province=text[:4]
    else:
        Province=text[:3]
    
    #获取目标数据
    table=article.find_all('table')
    
    table1=table[0]
    table2=table[1]
    
    tr1=table1.find_all('tr')
    tr2=table2.find_all('tr')
    del tr2[:3]

    all2019=tr1[-1].find_all('td')
    all2018=tr1[-2].find_all('td')
    all2017=tr1[-3].find_all('td')
    
    #目标数据写入
    csv_writer.writerow(["华北电力大学","2019",Province,"理科","all",all2019[3].get_text(),"09118126丁自超"])
    csv_writer.writerow(["华北电力大学","2019",Province,"文科","all",all2019[-2].get_text(),"09118126丁自超"])
    for i in range(len(tr2)):
        x=tr2[i].find_all('td')
        csv_writer.writerow(["华北电力大学","2019",Province,x[1].get_text(),x[0].get_text(),x[3].get_text(),"09118126丁自超"])
    
    csv_writer.writerow(["华北电力大学","2018",Province,"理科","all",all2018[3].get_text(),"09118126丁自超"])
    csv_writer.writerow(["华北电力大学","2018",Province,"文科","all",all2018[-2].get_text(),"09118126丁自超"])
    for i in range(len(tr2)):
        x=tr2[i].find_all('td')
        csv_writer.writerow(["华北电力大学","2018",Province,x[1].get_text(),x[0].get_text(),x[6].get_text(),"09118126丁自超"])
    
    csv_writer.writerow(["华北电力大学","2017",Province,"理科","all",all2017[3].get_text(),"09118126丁自超"])
    csv_writer.writerow(["华北电力大学","2017",Province,"文科","all",all2017[-2].get_text(),"09118126丁自超"])
    for i in range(len(tr2)):
        x=tr2[i].find_all('td')
        csv_writer.writerow(["华北电力大学","2017",Province,x[1].get_text(),x[0].get_text(),x[-2].get_text(),"09118126丁自超"])
    
for url in urls:
    html = get_html(url)
    analyse_html(html)    

file.close()
    
    