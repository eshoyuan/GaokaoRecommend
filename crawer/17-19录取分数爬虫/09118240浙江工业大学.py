import requests
from bs4 import BeautifulSoup
import pandas as pd

import re

def getsoup(url):
    '''
    参数
    ----------
    url : str,要爬取链接.

    soup : BeautifulSoup,抓取的网页数据.
    '''
    r = requests.get(url)
    #将从内容中分析出来的编码方式作为编码
    r.encoding = r.apparent_encoding
    soup=BeautifulSoup(r.text,'html.parser')
    return soup



def year_data(soup,year):
    '''
    参数
    ----------
    soup : BeautifulSoup,抓取的网页数据.
    year : str,想要抓取得年份.

    返回
    -------
    babysoup : BeautifulSoup,抓取的对应年份数据.
    '''
    #查看该网页所有的超链接
    babylink=soup.find_all('a')
    
    for i in babylink:
        #通过标题来判断
        if i.get('title') ==year+'年浙江工业大学外省招生录取情况汇总表':
            newurl=i.get('href')
            #参看子链接的形式，以便修正url的正确路径
            print(year,'年的子链接为',newurl)
            newurl=prefix_url+newurl.split('..')[-1]
            
    babysoup=getsoup(newurl)
    
    return babysoup




def get_tr_2019(soup):
    '''
    参数
    ----------
    soup : BeautifulSoup,对应年份的数据.

    返回
    -------
    data[2:] : list,指定从表格里取得的数据，[2:]去除表头.
    '''
    data=[]
    #查找所有的表格

    trs = soup.find('tbody').find_all('tr')
    for i in trs:
        
        line = []
        for td in i.find_all('td'):
            #转为str，同时去除其中的换行符
            try:
                atom=td.span.string
                if atom !='\n':
                    line.append(atom)
            except:
                continue
        print(line)    
        data.append(line)
        

    return data
def get_tr(soup):
    '''
    参数
    ----------
    soup : BeautifulSoup,对应年份的数据.

    返回
    -------
    data[2:] : list,指定从表格里取得的数据，[2:]去除表头.
    '''
    data=[]
    #查找所有的表格

    trs = soup.find('tbody').find_all('tr')
    for i in trs:
        
        line = []
        for td in i:
            #转为str，同时去除其中的换行符
            try:
                atom=td.get_text()
                a = re.compile(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\t|\r')
                atom = a.sub('', atom)
                if atom !='\n':
                    line.append(atom)
            except:
                continue
        print(line)    
        data.append(line)
        

    return data



def make_pd_2019(data,year,df):
    '''
    参数
    ----------
    data : list,从网页表格中取得的数据.
    year : str,对应的年份.
    df : pandas,用来储存数据的全局变量.

    '''
    College='浙江工业大学'
    Year=year
    Major='all'
    Contributor='王明扬'
    Province=''
    Category=''
    Score=''
    for i in data:


        if len(i)>10:
            Province=i[0]
            rest=i[1:]
            
        else:
            rest=i
            
        
        #判断理科文科，去除预科、国家专项等
        if rest[0]=='理':
            Category='理科'
        elif rest[0]=='文':
            Category='文科'
       
        else:
            continue
        
        Score=rest[7]
        df=df.append({'College':College,'Year':Year,'Province':Province,'Category':Category,'Major':Major,'Score':Score,'Contributor':Contributor},
                     ignore_index=True)
    return df

def make_pd(data,year,df):
    '''
    参数
    ----------
    data : list,从网页表格中取得的数据.
    year : str,对应的年份.
    df : pandas,用来储存数据的全局变量.

    '''
    College='浙江工业大学'
    Year=year
    Major='all'
    Contributor='王明扬'
    Province=''
    Category=''
    Score=''
    for i in data:


        if len(i)>11:
            Province=i[1]
            rest=i[2:]

        else:
            rest=i
            
        #判断理科文科，去除预科、国家专项等
        if rest[0]=='理':
            Category='理科'
        elif rest[0]=='文':
            Category='文科'
        
        else:
            continue
        Score=rest[7]
        
        df=df.append({'College':College,'Year':Year,'Province':Province,'Category':Category,'Major':Major,'Score':Score,'Contributor':Contributor},
                     ignore_index=True)
    return df




if __name__ == "__main__":
    #建立空表格
    total_df=pd.DataFrame(columns=('College','Year','Province','Category','Major','Score','Contributor'))
    
    #设置网页前缀为浙江工业大学的本科招生网
    prefix_url='http://zs.zjut.edu.cn'
    totalurl=prefix_url+'/zsnews/html/b28p1.html'

    totalsoup=getsoup(totalurl)
        
#从主页面分别获取近三年的网页信息，提取并处理表格数据
soup=year_data(totalsoup,'2019')
data=get_tr_2019(soup)
total_df=make_pd_2019(data,'2019',total_df)
#保存文件，指定编码以及去除索引
total_df.to_csv('C:/Users/asus/Desktop/09118240王明扬-浙江工业大学.csv',encoding='utf_8_sig',index=None)

soup=year_data(totalsoup,'2018')
data=get_tr(soup)
total_df=make_pd(data,'2018',total_df)
#保存文件，指定编码以及去除索引
total_df.to_csv('C:/Users/asus/Desktop/09118240王明扬-浙江工业大学.csv',encoding='utf_8_sig',index=None)

soup=year_data(totalsoup,'2017')
data=get_tr(soup)
total_df=make_pd(data,'2017',total_df)
#保存文件，指定编码以及去除索引
total_df.to_csv('C:/Users/asus/Desktop/09118240王明扬-浙江工业大学.csv',encoding='utf_8_sig',index=None)