import requests
import time
import json
import csv
from bs4 import BeautifulSoup
# year 2019-2016
# province 55-85
err=0  # 用于确认数据爬取过程是否完整
data_list = []  # 用于存放每一项数据
for y in range(2016,2020): # 2016，2017，2018，2019 四年的数据
    for p in range(55,86):
        baseurl = ('http://sjcx.dlmu.edu.cn/home/ApiStudent/scoreMajorList?')
        params = {'year':y ,'province_id':p ,'subject_id':'','major_id':''}
        r = requests.get(baseurl,params=params)
        r.encoding='utf-8'
        j = json.loads(r.text) # 转化为json格式
        time.sleep(2)  # 增加延迟
        if (j.get('status')):
            print(y, p, 'done')
        else:
            err = 1
        for entry in j.get("data"):  # 整理数据格式
            if(entry.get('batch')=="本科一批"):  # 筛选只要本科一批的数据
                data_list.append({
                    'College': '大连海事大学',
                    'Year': entry.get('year'),
                    'Province': entry.get('province'),
                    'Category': entry.get('subject'),
                    'Major': entry.get('major'),
                    'Score': entry.get('score_line'),
                    'Contributor': '09118206陶特'
                })
if(err==0):
            print('all done')
print(data_list)

#newline的作用是防止每次插入都有空行
with open("09118206陶特-大连海事大学.csv", "a+", newline='') as csvfile:
        writer = csv.writer(csvfile)
        #以读的方式打开csv 用csv.reader方式判断是否存在标题。
        with open("09118206陶特-大连海事大学.csv", "r", newline="") as f:
            reader = csv.reader(f)
            if not [row for row in reader]:
                writer.writerow(data_list[0].keys())
                for ele in data_list:
                    writer.writerow(ele.values())
            else:
                for ele in data_list:
                    writer.writerow(ele.values())

def save_to_csv(lst):
    with open('09118206 陶特.csv','w',newline='',encoding='utf-8')as f:
        f_csv = csv.writer(f)
        for data in lst:
            f_csv.writerow(data)
# soup = BeautifulSoup(r.text,'html.parser')
