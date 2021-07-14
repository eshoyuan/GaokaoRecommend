import requests
p=['湖南','湖北','广东','广西','河南','河北','山东','山西','江苏','浙江','江西','黑龙江','新疆','云南','贵州','福建','吉林','安徽','四川','西藏','宁夏','辽宁','青海','甘肃','陕西','内蒙古','北京','上海','天津']
u1=["&scoreLineYear=2019&year=","&type=1"]
y=['2019','2018','2017']
url = "http://admission1.jiangnan.edu.cn/historyScore/getPageData?province=%E6%B1%9F%E8%8B%8F&scoreLineYear=2019&year=2019&type=1" 

def responce(url):
    r=requests.post(url)
    r=r.text
    r=eval(r)
    r=r["xlq"]
    return r

with open("D:/09118224祁畅-江南大学.csv",'w') as f:  
    writer = csv.writer(f)
    writer.writerow(['College','Year','Province','Category','Major','Score','Contributor']) 
    for j in range(len(y)):
        u=y[j].join(u1)
        u2=["http://admission1.jiangnan.edu.cn/historyScore/getPageData?province=",u]
        for i in range(len(p)):
            url=p[i].join(u2)
            r=responce(url)
            for t in range(len(r)):  
                writer.writerow(['江南大学',y[j],p[i],r[t]['type'],r[t]['name'],r[t]['lowScore'],'09118224祁畅']) 