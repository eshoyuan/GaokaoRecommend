import requests
import pandas as pd 


url='http://zsservice.nuaa.edu.cn/zsw-admin/api/getAdmissionScore?&page=1&limit=10'
#直接爬取网页上所有的信息，注意网站情况
result=requests.get(url)
result=result.text.replace("null","123")#将字符串中的null转换成字典可以处理的123,因为none同样不能被处理
result=eval(result)
#print(result['data'])进行检测
data=[]

for information in result['data']:
    if information['type']=='普通类':
        #只选取普通类的学生
        school_data={'College':'南京航空航天大学','Contributor':'09118226 李辰浩'}
        school_data['Year']=information['year']
        school_data['Category']=information['subject']
        school_data['Major']=information['specialty']
        school_data['Score']=information['lowestScore']
        school_data['Province']=information['province']
        data.append(school_data)

result_list=pd.DataFrame(data,columns=['College','Year','Province','Category','Major','Score','Contributor'])
result_list.sort_values(by=['C','B'],axis=0,ascending=False)#对网站上杂乱的数据进行排序
result_list.to_csv('09118226李辰浩_result.csv',index=False,encoding='gbk')