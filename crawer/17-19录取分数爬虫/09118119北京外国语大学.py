import pandas as pd
import requests

url='https://bwzs.bfsu.edu.cn/f/ajax_lnfs?ts=1589639715922'

# parameters initialization
location=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
year=['2019','2018','2017']
subject=['文史','理工','综合改革']

# define a dict to carry data
data={}
data_carrier=[]

# for every location
for l in location:
    data['ssmc']=l
    # for every year
    for y in year:
        data['zsnf']=y
        # for every subject
        for s in subject:
            data['klmc']=s
            data['zslx']='统招一批'
            
            response=requests.get(url,params=data)
            information=eval(response.text)
            information=information['data']['sszygradeList']

            for i in information:
                carry={'College':'北京外国语大学','Contributor':'09118119黄一凡'}
                carry['Year']=i['nf']
                carry['Province']=i['ssmc']
                carry['Major']=i['zymc']
                carry['Score']=i['minScore']

                signal=data['klmc']
                if signal=='文史':
                    carry['Category']='文科'
                if signal=='理工':
                    carry['Category']='理科'
                if signal=='综合改革':
                    carry['Category']='all'

                data_carrier.append(carry)

            print(l,y,s,'sucess')

# transform data to csv form
result=pd.DataFrame(data_carrier,columns=['College','Year','Province','Category','Major','Score','Contributor'])
result.to_csv('result.csv',index=False,encoding='gbk')
print('finish')