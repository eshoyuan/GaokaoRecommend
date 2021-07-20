import csv
import requests
from urllib import parse
import json
from bs4 import BeautifulSoup 
import random


def get_user_agent_pc():
    '''随机获得伪装头'''
    # pc端的user-agent
    user_agent_pc = [
        # 谷歌
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.html.2171.71 Safari/537.36',
        'Mozilla/5.0.html (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.html.1271.64 Safari/537.11',
        'Mozilla/5.0.html (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.html.648.133 Safari/534.16',
        # 火狐
        'Mozilla/5.0.html (Windows NT 6.1; WOW64; rv:34.0.html) Gecko/20100101 Firefox/34.0.html',
        'Mozilla/5.0.html (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        # opera
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.html.2171.95 Safari/537.36 OPR/26.0.html.1656.60',
        # qq浏览器
        'Mozilla/5.0.html (compatible; MSIE 9.0.html; Windows NT 6.1; WOW64; Trident/5.0.html; SLCC2; .NET CLR 2.0.html.50727; .NET CLR 3.5.30729; .NET CLR 3.0.html.30729; Media Center PC 6.0.html; .NET4.0C; .NET4.0E; QQBrowser/7.0.html.3698.400)',
        # 搜狗浏览器
        'Mozilla/5.0.html (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.html.963.84 Safari/535.11 SE 2.X MetaSr 1.0.html',
        # 360浏览器
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.html.1599.101 Safari/537.36',
        'Mozilla/5.0.html (Windows NT 6.1; WOW64; Trident/7.0.html; rv:11.0.html) like Gecko',
        # uc浏览器
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.html.2125.122 UBrowser/4.0.html.3214.0.html Safari/537.36',
    ]
    return random.choice(user_agent_pc)

def spider():
    '''迭代爬取西北大学某年-某文理科-某省份-某专业的最低分数线'''
    #Init
    csv_list=list()
    info_list=list()
    year_list=['2019','2018','2017','2016']#业务要求四年的分数，2016为可选内容
    province_list=['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江',
                   '上海', '江苏', '浙江', '安徽', '福建', '江西','山东', '河南', '湖北',
                   '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏',
                   '陕西', '甘肃', '青海', '宁夏', '新疆']#31个招生的省市
    for y in (year_list):
        #按年迭代
        if (y=='2019') or (y=='2018'):
            major_list=['文史','理工']
        else:
            #16、17年的url与18、19年不同
            major_list=['文科','理科']
        for m in major_list:
            #按文理迭代
            major_dict={'scienceClass':'{}'.format(m)}
            major_url=parse.urlencode(major_dict)
            for p in range(len(province_list)):
                #按省迭代
                cityname_dict={'cityName':'{}'.format(province_list[p])}
                cityname_url=parse.urlencode(cityname_dict)
                #print(cityname_url)
                #加上随机伪装头
                try:
                    #异常处理
                    r=requests.get("http://admin.zhinengdayi.com/front/enroll/findMajorScoreCompareList?sCode=FCHTWR&{}&year={}&{}&type={}&batch={}".format(cityname_url,y,major_url,'%E6%99%AE%E9%80%9A%E6%96%87%E7%90%86','%E6%9C%AC%E7%A7%91%E4%B8%80%E6%89%B9')
                              ,headers={
                    'User-Agent': get_user_agent_pc()})
                    jsonlib=r.json()
                except:
                    print("Spider of {}-{}-{} went wrong!".format(y,m,province_list[p]))
                    break
                for index in range(len(jsonlib['list'])):
                    info_list=[]
                    info_string="西北大学,{},{},{},{},{},61518407李浩瑞".format(y,province_list[p],m,jsonlib['list'][index]['majorName'],int(jsonlib['list'][index]['lowScore']))
                    #作业要求“文科”和“理科”，因此进行字符串替换
                    info_string=info_string.replace('文史','文科')
                    info_string=info_string.replace('理工','理科')
                    info_list=info_string.split(",")
                    csv_list.append(info_list)
    return csv_list

def write_csv(csv_list):
    '''
    将爬取到的信息写入csv文件中
    csv_list:按"学校-年份-省份-文理-专业-得分-贡献值者"排列的二维数组
    '''
    s_head="College Year Province Category Major Score Contributor"#写入表头
    csv_head=[]
    csv_head=s_head.split(" ")
    with open('61518407李浩瑞-西北大学.csv', 'w', newline='') as csvfile:
        #写入表单数据
        writer  = csv.writer(csvfile)
        writer.writerow(csv_head)
        for row in csv_list:
            writer.writerow(row)
            
if __name__=="__main__":
    csv_list=spider()#爬取数据存入列表
    write_csv(csv_list)#写入文件
    print("Finish!")