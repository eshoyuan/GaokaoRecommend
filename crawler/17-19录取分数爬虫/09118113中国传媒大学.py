import requests
import json
import random
import pandas as pd

def getreponse(data):
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
    url='http://zszx.cuc.edu.cn/f/ajax_lnfs'
    Cookie="zhaosheng.cuc.session.id=3b3cb4e2a2f84caabc7b6e728d246257; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1589445237,1589683123; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1589683123"
    headers = {
            'User-agent': random.choice(USER_AGENTS), #设置get请求的User-Agent，用于伪装浏览器UA 
            'Cookie': Cookie,
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'zszx.cuc.edu.cn',
            'Referer': 'http://zszx.cuc.edu.cn/static/front/cuc/basic/html_web/lnfs.html'
            }
    reponse=requests.post(url,data=data,headers=headers)
    return reponse

def getlist(reponse):
    json_list=json.loads(reponse.content) 
    y=[]
    for temp in json_list['data']['sszygradeList']:
        if(temp['klmc']=='理工'):
            a='理科'
        if(temp['klmc']=='文史'):
            a='文科'
        if(temp['klmc']=='综合改革'):
            a='all'
        x=['中国传媒大学',temp['nf'],temp['ssmc'],a,temp['zymc'],temp['minScore'],'09118113曹思辰']
        y.append(x)
    return y

def getdata():
    data=[]
    province=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
    year=['2019','2018','2017']
    category=['理工','文史','综合改革']
    genre=['普通类']
    for temp1 in province:
        for temp2 in year:
            for temp3 in category:
                for temp4 in genre:
                    tempdata={'ssmc': temp1,                             
                              'zsnf': temp2,
                              'klmc': temp3,
                              'zslx': temp4
                              }
                    data.append(tempdata)
    return data

def getcsv(List):
    df = pd.DataFrame(List, columns=['College','Year','Province','Category','Major','Score','Contributor']) 
    out_path='09118113曹思辰-中国传媒大学.csv'
    df.to_csv(out_path,index=False,header=True,encoding = 'gbk') #按指定列名顺序输出df    
           
def main():
    data=getdata()
    List=[]
    for temp in data:
        reponse=getreponse(temp)
        templist=getlist(reponse)
        List.extend(templist)
    getcsv(List)
    
if __name__ == '__main__':
    main()