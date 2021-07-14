#!/usr/bin/env python
# coding: utf-8

# In[1]:


#原本分配的大学中南财经政法大学招生网站出了问题，因此改为湖北大学

import requests
import pandas as pd


url_list = ['http://zsxx.hubu.edu.cn/info/1019/1929.htm',
            'http://zsxx.hubu.edu.cn/info/1019/1802.htm',
            'http://zsxx.hubu.edu.cn/info/1019/1661.htm']
def infoGet():
    """
    湖北大学招生网站的录取分数线为表格形式排版
    因此直接读取网站信息并用pandas的read_html()函数解析即可获取所需信息
    """
    html = []
    for i in url_list:
        r = requests.get(i).content.decode('utf-8')
        df=pd.read_html(r)
        html.append(df[0])
    return html

def infoSelect(a):
    """
    将爬取到的信息筛选，保留需要的信息
    """
    index = [1,4,8]
    score = []
    for i in index:
        score.append(list(a[i]))
    return score

def infoSave(html):
    contributor = '09118241陈嘉源'
    college = '湖北大学'
    major = 'all'#该校招生网站分数线不分专业
    special = ["上海","浙江"]#上海与浙江在2019年与2018年是综合改革
    for i in range(3):
        html[i]=infoSelect(html[i])
    df = pd.DataFrame(columns=('College','Year','Province','Category','Major','Score','Contributor'))
    for j in range(3):#年份
        for k in range(len(html[j][0])-2):
            if html[j][0][k+2] in special and not(j == 2):
                category = "综合改革"
                df = df.append([{'College':college,
                             'Year':2019-j,
                             'Province':html[j][0][k+2],
                             'Category':category,
                             'Major':major,
                             'Score':html[j][1][k+2],
                             'Contributor':contributor
                                }])
            else:
                category1 = "文科"
                category2 = '理科'
                df = df.append([{'College':college,
                             'Year':2019-j,
                             'Province':html[j][0][k+2],
                             'Category':category1,
                             'Major':major,
                             'Score':html[j][1][k+2],
                             'Contributor':contributor
                               }])
                df = df.append([{'College':college,
                             'Year':2019-j,
                             'Province':html[j][0][k+2],
                             'Category':category2,
                             'Major':major,
                             'Score':html[j][2][k+2],
                             'Contributor':contributor
                                }])
    df.to_csv('09118241陈嘉源-湖北大学.csv', encoding='utf-8',index=False)
    
if __name__ == "__main__":
    k = []
    k = infoGet()
    infoSave(k)






