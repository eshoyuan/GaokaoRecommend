# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:22:48 2020

@author: 张淼森
"""
from bs4 import BeautifulSoup
import requests
import csv
#检查ul地址
def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法链接服务器！！！')

#爬取资源
def get_contents(ulist,rurl):
    soup = BeautifulSoup(rurl,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)
        
def get_link(ulist,rurl):
    soup = BeautifulSoup(rurl,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = dict()
        for td in tr:
            if td != None:
                tt = str(td).split('\"')
                key = ''
                info = ''
                for i in tt:
                    if i[0] == '>' and i.find('</a>')!=-1:
                        key = i[1:i.find('</a>')]
                    if i[0] == 'h':
                        info = i
                if key != '':
                    ui[key] = info
        ulist.append(ui)
    st = dict()
    for it in ulist:
        st.update(it)
    return st
    #ulist = st
#修改数据
def to_list(name,urli,year):
    l = []
    for item in urli:
        item = [item[i] for i in range(len(item)) if item[i]!='\n']
        item = [item[i] for i in range(len(item)) if item[i]!=None]
        if item == []:
            continue
        itc = ['西安电子科技大学',year,name,'理科',]
        for i in range(2):
            tbc = item[i]
            tb = str(tbc)
            tb = tb.replace('\t','')
            tb = tb.replace('\n','')
            tb = tb.replace('\r','')
            tb = tb.replace('省','')
            itc.append(tb)
        itc.append('61518428张淼森')
        if itc[4]!='专业' and itc[4]!='\xa0':
             l.append(itc)
    return l

def save_file(res_list):
    c = open("61518428张淼森-西安电子科技大学.csv",'w',newline='')
    writer = csv.writer(c)
    writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])
    for row in res_list:
        writer.writerow(row)


def main():
    url_dict = {'2019':"https://zsb.xidian.edu.cn/html/zsxx/lnfs/2019/1129/1221.html",
                '2018':"https://zsb.xidian.edu.cn/html/zsxx/lnfs/2019/0122/1106.html",
                '2017':"https://zsb.xidian.edu.cn/html/zsxx/lnfs/2017/1115/956.html"}
    res_list = []
    for key in url_dict.keys():
        urli = []
        url = url_dict[key]
        rs = check_link(url)
        links = get_link(urli,rs) 
        for suburls in links.keys():
            content = []
            rs = check_link(links[suburls])
            get_contents(content,rs)
            res_list.extend(to_list(suburls,content,key))
    save_file(res_list)


main()

 

 
