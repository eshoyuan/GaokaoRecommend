import requests
from bs4 import BeautifulSoup
import pandas as pd



def getsoup(url):
    '''
    参数
    ----------
    url : str,要爬取链接.

    返回
    -------
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
        if i.get('title') =='华中农业大学'+year+'年各省录取分数情况统计':
            newurl=i.get('href')
            #参看子链接的形式，以便修正url的正确路径
            print(year,'年的子链接为',newurl)
            newurl=prefix_url+newurl.split('..')[-1]
            
    babysoup=getsoup(newurl)
    
    return babysoup




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
    trs = soup.find_all('tr')
    for tr in trs:
        line = []
        for td in tr:
            #转为str，同时去除其中的换行符
            atom=td.string
            if atom !='\n':
                line.append(atom)
        data.append(line)
        
    #去掉表头
    return data[2:]




def make_pd(data,year,df):
    '''
    参数
    ----------
    data : list,从网页表格中取得的数据.
    year : str,对应的年份.
    df : pandas,用来储存数据的全局变量.

    返回
    -------
    df : pandas,添加新数据后的pandas.
    '''
    College='华中农业大学'
    Year=year
    Major='all'
    Contributor='卢甲浩'
    Province=''
    Category=''
    for i in data:
        '''
        原表格的格式为
        港澳台|理工|400| ——| ——|
              |文史|400|426|403|
        '''
        if len(i)>4:
            Province=i[0]
            rest=i[1:]
        else:
            rest=i
        
        #判断理科文科综合，去除预科、国家专项等
        if rest[0]=='理工':
            Category='理科'
        elif rest[0]=='文史':
            Category='文科'
        elif rest[0]=='综合':
            Category='综合' 
        else:
            continue
        
        #去除未招生项
        if rest[-1]!='—':
            Score=rest[-1]
        else:
            continue
        
        
        df=df.append({'College':College,'Year':Year,'Province':Province,'Category':Category,'Major':Major,'Score':Score,'Contributor':Contributor},
                     ignore_index=True)
    return df




if __name__ == "__main__":
    #建立空表格
    total_df=pd.DataFrame(columns=('College','Year','Province','Category','Major','Score','Contributor'))
    
    #设置网页前缀为华中农业大学的本科招生网
    prefix_url='http://zs.hzau.edu.cn'
    totalurl=prefix_url+'/xxgk/lqjggk.htm'

    totalsoup=getsoup(totalurl)
    
    years=['2017','2018','2019']
    for year in years:
        #从主页面分别获取近三年的网页信息，提取并处理表格数据
        soup=year_data(totalsoup,year)
        data=get_tr(soup)
        total_df=make_pd(data,year,total_df)
    #保存文件，指定编码以及去除索引
    total_df.to_csv('C:/Users/Lurejahor/Desktop/09118243卢甲浩-华中农业大学.csv',encoding='utf_8_sig',index=None)