import requests
import random
from bs4 import BeautifulSoup
import csv


# 下面是代理列表，随机选择
USER_AGENTS = [
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)"
        ]

# 推荐Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11
# 推荐Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0
# 推荐Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)
# 推荐Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)



# 网页所需的header
headers = {
    'User-agent': random.choice(USER_AGENTS),
    'Cookie': 'ASP.NET_SessionId=z5wbkj2krexle4rafvjuwn55',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'bkzswd.swu.edu.cn',
    'Referer': 'http://bkzswd.swu.edu.cn/ksk/lq_lnfscx.aspx'
}

# 网页所需的data
data = {
        'ctl00$ScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel2|ctl00$ContentPlaceHolder1$klmc_dd',
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$klmc_dd',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': '00072523',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': 'us6eh7UxgjC6nD46Onx0exrpltGL30De881FM5f44D5aGzEK9BGCtiFSJigF6ObK6y6qSsTF3nmxZ55yrL+3MvAIWU6O9FT8VFsZ8uY4IWn2ySBWF994v0UlALVAdPoudoMYiUhV0F1GQMkfBdFwISrBP9Z2AGOTEZ9BYKMdsOQ9M1iFoDRZpHqXNP4wcZ639AVp3Uw4lWFu7krVgDnlFliC3OW2TajXULQIXCF6dCMt43DLZGIJZSDv6QpEeCNiJmnrfc6f+IxPbZrZKL8MVvg8h/S3EZhkadGWPdOxOR5D3VwcsEXF8uWkje2OALxlz9n2n4UjO73KJbEuNyhqPSjpwT2knrc7vhXofeYHX/G26QVOnTF5obMQsWbpxIQw+6b38eEIPbCSKh++e2KRqQ5vHK40y5tW05+j69tZRRtDpqZEwP3fxMvXe1a/tGOKAV9KNrtNwD9qrIV1FK8XSyKAfWw=',
        'ctl00$ContentPlaceHolder1$year_dd': '',
        'ctl00$ContentPlaceHolder1$ssmc_dd': '',
        'ctl00$ContentPlaceHolder1$klmc_dd': ''
      }

# 这所学校招生的省份
province = ["安徽", "北京", "福建", "甘肃", "广东", "广西", "贵州", "海南", "河北",
            "河南", "黑龙江", "湖北", "湖南", "吉林", "江苏", "江西", "辽宁", "内蒙古", "宁夏",
            "青海", "山东", "山西", "陕西", "上海", "四川", "天津", "西藏",
            "新疆", "云南", "浙江", "重庆", ]

# 科类
discipline = ["理工", "文史"]

# 年份
year = ["2019", "2018", "2017", "2016"]

url = 'http://bkzswd.swu.edu.cn/ksk/lq_lnfscx.aspx'   # 要爬取的网页

def getHTMLText(url, data, header):
    '''
    获取网页html的函数
    :param url: 要获取的网页
    :param data: data
    :param header: header
    :return: post获得的text
    '''
    try:
        print(headers.get('User-agent'))
        r = requests.post(url, data=data, headers=headers)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取网页时出现错误！")
        return ""

def fillUnivList(ulist, html):
    '''
    将html内容存入列表的函数
    :param ulist: 将页面获取的内容放入列表
    :param html:
    :return: 返回处理好的列表
    '''
    temp = []
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find_all('td'):
        tds = str(tr)[4:-5].strip()        # 获得的数据有转义字符，这里对其进行删除
        temp.append(tds)
    for i in range(0, len(temp), 9):
        app_temp = ["西南大学"]             # 获取的信息没有学校名称，这里手动添加
        for j in range(i, i+9):
            app_temp.append(temp[j])
        app_temp.append("09118144杜熙源")
        ulist.append(app_temp)
    return ulist

def printUnivList(ulist):
    '''
    打印获取的列表，主要为了方便查看和检查是否有问题
    :param ulist: 要打印的列表
    :param num: 想打印多少个
    '''
    tplt = "{0:^10}\t{1:{10}^10}\t{2:^10}\t{3:^10}\t{4:{10}^10}\t{5:^10}\t{6:^10}\t{7:{10}^10}\t{8:^10}\t{9:^10}"
    print(tplt.format("学校", "年份", "省份", "批次", "科类", "专业", "录取人数", "最高分", "最低分", "校区", chr(12288)))
    num = len(ulist)
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], chr(12288)))

def WriteToCsv(ulist):
    '''
    写入csv文件的函数
    :param ulist: 要写入csv文件的列表
    '''
    file = open('09118144杜熙源-西南大学.csv', 'a', newline="")
    csv_writer = csv.writer(file)
    for i in range(len(ulist)):
        csv_writer.writerow(ulist[i])
    file.close()

def main():
    url = 'http://bkzswd.swu.edu.cn/ksk/lq_lnfscx.aspx'
    file = open('09118144杜熙源-西南大学.csv', 'w', newline="")
    csv_writer = csv.writer(file)
    csv_writer.writerow(["College", "Year", "Province", "Batch",
                         "Category", "Major", "Number of applicants",
                         "Highest score", "Score", "Campus", "Contributor"])  # 添加表头
    file.close()
    for i in year:
        for j in province:
            for k in discipline:
                # 遍历这三个列表，获取对应的信息
                uinfo = []
                data['ctl00$ContentPlaceHolder1$year_dd'] = i
                data['ctl00$ContentPlaceHolder1$ssmc_dd'] = j
                data['ctl00$ContentPlaceHolder1$klmc_dd'] = k
                html = getHTMLText(url, data=data, header=headers)
                fillUnivList(uinfo, html)
                printUnivList(uinfo)
                WriteToCsv(uinfo)

if __name__ == "__main__":
    main()

