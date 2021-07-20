import requests
from bs4 import BeautifulSoup
import pandas as pd

# 爬取网页
def GetHtml(url):
    try:
        # 这里需要使用verify=False关闭SSL安全验证
        r = requests.get(url, headers = {'user-agent':'Mozilla/5.0'}, timeout = 30, verify = False)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print('error')
        return ""

# 用于存放数据的列表
list=[]

def Craw(year, province, url):
    # 爬取并解析网页
    html = GetHtml(url)
    soup = BeautifulSoup(html,'html.parser')
    # 分数数据在第16个表格中
    tables = soup.findAll('table')
    score = tables[15]
    # 每一行对应一个专业
    majors = score.findAll('tr')
    # 各个年份最低分对应位置不同
    loc = 2
    if year == 2018:
        loc = 4
    elif year == 2017:
        loc = 5
    elif year == 2016:
        loc = 2
    for major in majors:
        # 读取专业的每一个数据
        contents = major.findAll('p')
        if(len(contents) > loc):
            # 网页文理科使用的是理工和文史，这里把它替换成理科和文科
            if contents[1].text == "理工" :
                # 网页中有数据后多加了一个逗号和空格，所以用到了strip(',')
                print(contents[0].text, '理科', ":", contents[loc].text.strip(', '))
                list.append(['长安大学', str(year), province, '理科', contents[0].text, contents[loc].text.strip(', '), '61518424王贵涛'])
            if contents[1].text == "文史":
                print(contents[0].text, '文科', ":", contents[loc].text.strip(', '))
                list.append(['长安大学', str(year), province, '文科', contents[0].text, contents[loc].text.strip(', '), '61518424王贵涛'])

# 所有省份和对应的编码
ProvinceList = [
        ("1",  "北京",  '%B1%B1%BE%A9'),
        ("2",  "天津",  '%CC%EC%BD%F2'),
        ("3",  "上海",  '%C9%CF%BA%A3'),
        ("4",  "重庆",  '%D6%D8%C7%EC'),
        ("5",  "黑龙江",'%BA%DA%C1%FA%BD%AD'),
        ("6",  "吉林",  '%BC%AA%C1%D6'),
        ("7",  "辽宁",  '%C1%C9%C4%FE'),
        ("8",  "内蒙古",'%C4%DA%C3%C9%B9%C5'),
        ("9",  "河北",  '%BA%D3%B1%B1'),
        ("10", "河南",  '%BA%D3%C4%CF'),
        ("11", "山东",  '%C9%BD%B6%AB'),
        ("12", "山西",  '%C9%BD%CE%F7'),
        ("13", "陕西",  '%C9%C2%CE%F7'),
        ("14", "甘肃",  '%B8%CA%CB%E0'),
        ("15", "宁夏",  '%C4%FE%CF%C4'),
        ("16", "青海",  '%C7%E0%BA%A3'),
        ("17", "新疆",  '%D0%C2%BD%AE'),
        ("18", "西藏",  '%CE%F7%B2%D8'),
        ("19", "云南",  '%D4%C6%C4%CF'),
        ("20", "贵州",  '%B9%F3%D6%DD'),
        ("21", "四川",  '%CB%C4%B4%A8'),
        ("22", "湖南",  '%BA%FE%C4%CF'),
        ("23", "湖北",  '%BA%FE%B1%B1'),
        ("24", "广东",  '%B9%E3%B6%AB'),
        ("25", "广西",  '%B9%E3%CE%F7'),
        ("26", "江苏",  '%BD%AD%CB%D5'),
        ("27", "江西",  '%BD%AD%CE%F7'),
        ("28", "安徽",  '%B0%B2%BB%D5'),
        ("29", "浙江",  '%D5%E3%BD%AD'),
        ("30", "福建",  '%B8%A3%BD%A8'),
        ("31", "海南",  '%BA%A3%C4%CF'),
        ("32", "台湾",  '%CC%A8%CD%E5'),
        ("33", "香港",  '%CF%E3%B8%DB'),
        ("34", "澳门",  '%B0%C4%C3%C5'),
]

# 爬取2016~2018年的数据，2019年的分数是以图片形式存在
for year in range(2016, 2019):
    for province in ProvinceList:
        url = 'http://zsb.chd.edu.cn/search_lnfs_view.asp?nianfeng=' + str(year) + '&province=' + province[2]
        print(str(year) + '年' + province[1] + '省:', url)
        Craw(year, province[1], url)

# 将列表转化为dataframe，添加上类别，并保存为csv格式
df = pd.DataFrame(list, columns=('College', 'Year', 'Province', 'Catagory', 'Major', 'Score', 'Contributor'))
print(df)
df.to_csv('61518424 王贵涛-长安大学.csv', index = False, encoding = 'utf-8-sig')
