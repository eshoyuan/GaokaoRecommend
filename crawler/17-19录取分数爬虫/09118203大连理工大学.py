import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# 获取三年，33个不同分类省份的列表
years = ['2019', '2018', '2017']
places = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林',
         '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西',
         '山东', '河南', '湖北', '湖南', '广东', '广西', '海南',
         '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃',
         '青海', '宁夏', '新疆', '西藏班', '新疆班']
College = []  # 大学名列表
Year = []  # 年份列表
Province = []  # 省份列表
Category = []  # 文，理或其他列表
Major = []  # 专业列表
Score = []  # 最低分列表
Contributor = []  # 收集者列表
school_name = '大连理工大学'  # 学校名
contributor = '09118203张雨'  # 收集者

# 遍历第i年的第j个地方
for year in years:
    for place in places:
        url = 'http://zsb.dlut.edu.cn/score'
        # 只需更改年份和地址，遍历所有的网页
        data1 = {'type': '0',
                 'profession': '',
                 'campus': '主校区',
                 'year': year,
                 'province': place}
        headers1 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '91',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'zsb.dlut.edu.cn',
            'Origin': 'http://zsb.dlut.edu.cn',
            'Referer': 'http://zsb.dlut.edu.cn/score',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        strhtml = requests.post(url, data1, headers1)
        # 通过BeautifulSoup库解析获取到的网页代码，讲表格部分提取出来，并存为school_data
        school = BeautifulSoup(strhtml.text, 'html.parser')
        school_data = school.find_all('td', {'class': 'text-center'})

        # 遍历school_data列表中的每一条数据
        i = 0
        while i < len(school_data):
            if 48 <= ord(school_data[i].string[0]) <= 57:
                if float(school_data[i].string) > 750:
                    if school_data[i + 2].string == '录取分数':
                        # 文理所有专业的最低分
                        Category.append(school_data[i + 1].string)
                        Major.append('all')
                        Score.append(school_data[i + 5].string)
                    else:
                        # 提取出文理、专业和专业录取最低分
                        Category.append(school_data[i + 1].string)
                        Major.append(school_data[i + 2].string)
                        Score.append(school_data[i + 5].string)
                    College.append(school_name)
                    Year.append(year)
                    Province.append(place)
                    Contributor.append(contributor)
                    # 转入下一条数据
                    i += 6
            else:
                i += 1

# 讲7个list转化为字典再转换为dataframe
data = {"College": College,
        "Year": Year,
        "Province": Province,
        "Category": Category,
        "Major": Major,
        "Score": Score,
        "Contributor": Contributor}
data = pd.DataFrame(data)
# 存储该dataframe为csv文件
outputpath = '/Users/zhangyu/Desktop/09118203张雨-大连理工大学.csv'
data.to_csv(outputpath, sep=',', index=False, header=True)
