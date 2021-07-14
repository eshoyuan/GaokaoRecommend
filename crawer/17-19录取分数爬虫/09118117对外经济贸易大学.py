import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import quote, unquote
import urllib.request
import json
import pandas as pd


getListURL="http://admin.zhinengdayi.com/front/enroll/getMajorSelectChange?cityName=%E5%8C%97%E4%BA%AC&sCode=NLGYFE"
listRequest=urllib.request.Request(getListURL)
allList=urllib.request.urlopen(listRequest).read().decode("utf-8")
listData=json.loads(allList)
yearList=listData["yearList"]
scienceList=listData['scienceList']
cityList=["北京", "天津", '河北','山西','内蒙古',
          '辽宁','吉林','黑龙江','上海','江苏','浙江','安徽',
          '福建','江西','山东', '河南', '湖北','湖南','广西',
          '广东','海南','重庆','四川','贵州','云南','西藏',
          '陕西','甘肃','青海', '宁夏', '新疆']

def getJSON(city, year, science):
    cityCode=quote(city)
    scienceCode=quote(science)
    response = urllib.request.Request('http://admin.zhinengdayi.com/front/enroll/findMajorScoreCompareList?sCode=NLGYFE&cityName={0}&year={1}&scienceClass={2}&type=%E6%99%AE%E9%80%9A%E6%8B%9B%E7%94%9F&batch='.format(cityCode, year,scienceCode))
    raw = urllib.request.urlopen(response).read().decode("utf-8")
    data=json.loads(raw)
    data=pd.DataFrame(data['list'])
    elementList=["majorName","year",'cityName', "scienceClass", "lowScore"]
    for i in data.columns:
        if i not in elementList:
            del data[i]
    return data
if __name__== '__main__':
    scoreData=[]
    scoreData=pd.DataFrame(scoreData)
    for i in cityList:
        for j in yearList:
            for k in scienceList:
                scoreData=scoreData.append(getJSON(i,j,k))
    scoreData.rename(columns={"majorName":'专业名','year':'年份','cityName':'省市名',
                              'scienceClass':'科类','lowScore':'录取分数线'})
    print(scoreData)
    scoreData.to_csv("对外经贸分数线.csv",index=None)
