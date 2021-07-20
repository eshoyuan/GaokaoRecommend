import requests
import json
import pandas as pd

# 获取页面源代码内容
# 根据观察，湖南师范大学页面源代码是json格式，所以直接转化为字典，并返回
def getHTMLtoDict(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        r_dict = json.loads(r.text)
        return r_dict
    except:
        return ""

# 读取中国各省名称，返回元素为省名的列表
def getProvinceName():
    pro_path = './61518122_丁自民_province.txt'
    f = open(pro_path, "r")
    pro_str = f.read()
    pro_list = pro_str.split('、')
    f.close()
    return pro_list

def main():
    http_1 = 'http://admin.zhinengdayi.com/front/enroll/findSchoolEnrollList?sCode=NJBCYO&cityName='
    http_2 = '&scienceClass='
    http_3 = '&type=&batch='
    sub_name = ['文史','理工']
    pro_name = getProvinceName()
    benchmark_info = [['University','Year','Province','Category','Major','Score','Contributor']]
    for pro in pro_name:
        for sub in sub_name:
            for i in range(0,5):
                try:
                    # 根据湖南师范大学招生信息网的网址特点，做如下设计
                    url = http_1 + pro + http_2 + sub + http_3
                    HNNU_dict = getHTMLtoDict(url)
                    if HNNU_dict['list'][i]['type'] == '普通文理':
                        benchmark_info.append(['湖南师范大学',HNNU_dict['list'][i]['year'],str(pro),str(sub),'all',HNNU_dict['list'][i]['lowScore'],'61518122丁自民'])
                except:
                    continue
    # 浙江，上海两地2019年高考部分文理科，网页科目关键词为“综合改革”
    for pro in ['浙江','上海']:
        sub = '综合改革'
        for i in range(0, 3):
            try:
                url = http_1 + pro + http_2 + sub + http_3
                HNNU_dict = getHTMLtoDict(url)
                if HNNU_dict['list'][i]['type'] == '普通文理':
                    benchmark_info.append(['湖南师范大学', HNNU_dict['list'][i]['year'], str(pro), 'all', 'all', HNNU_dict['list'][i]['lowScore'], '61518122丁自民'])
            except:
                continue
    benchmark_info_pd = pd.DataFrame(benchmark_info)
    benchmark_info_pd.to_csv('61518122_丁自民_第一次作业结果.csv')

main()
