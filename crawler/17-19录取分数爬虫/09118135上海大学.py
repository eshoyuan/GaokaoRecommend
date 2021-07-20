# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:44:37 2020

@author: pc089
"""
import requests
import random
import bs4
import csv

USER_AGENTS = [
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
        ]

years = [2019, 2018, 2017, 2016]
provinces = ['北京', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '新疆', '台湾', '香港', '澳门', '港澳台']

# 文件的建立及初始化
file = open('09118135王屹之-上海大学.csv','w', newline='')
csv_writer = csv.writer(file)
csv_writer.writerow(['Collage', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])

# 第一部分的信息爬取（2018-2019）
url1 = 'http://bks.shu.edu.cn/pub/scores.aspx'

headers1 = {
    'User-agent': random.choice(USER_AGENTS), 
    'Cookie': 'ASP.NET_SessionId=gja4btcx1ffu5wk4yllvtrwx',
    'Connection': 'keep-alive',
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'bks.shu.edu.cn',
    'Referer': 'http://bks.shu.edu.cn/pub/scores.aspx'
    }

data1 = {
    '__EVENTTARGET':'Panel1$ctl00$btnOK',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'/wEPDwUJLTQxNTE4OTQ4ZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBwUGUGFuZWwxBRRQYW5lbDEkY3RsMDAkU0NfWWVhcgUXUGFuZWwxJGN0bDAwJFNDX1NoZW5nWUQFF1BhbmVsMSRjdGwwMCRTQ19MZWlYaW5nBRRQYW5lbDEkY3RsMDAkU0NfS2VNWgUSUGFuZWwxJGN0bDAwJGJ0bk9LBQxQYW5lbDEkR3JpZDEFDFBhbmVsMSRHcmlkMQ8PZGVkQVC7R1A+7ftRxnMGX/Xac1cPEaVn/wb4nVmpSK4WlHo=',
    '__VIEWSTATEGENERATOR':'44F706D6',
    'Panel1$ctl00$SC_Year$Value':0, # year
    'Panel1$ctl00$SC_Year':0, # year
    'Panel1$ctl00$SC_ShengYD$Value':'', # province
    'Panel1$ctl00$SC_ShengYD':'', # province
    'Panel1$ctl00$SC_LeiXing$Value':'一本',
    'Panel1$ctl00$SC_LeiXing':'一本',
    'Panel1$ctl00$SC_KeMZ$Value':'全部',
    'Panel1$ctl00$SC_KeMZ':'全部',
    'F_TARGET':'Panel1_ctl00_btnOK',
    'Panel1_Grid1_Collapsed':'false',
    'Panel1_Collapsed':'false',
    'F_STATE':'eyJQYW5lbDFfY3RsMDBfU0NfWWVhciI6eyJGX0l0ZW1zIjpbWyIyMDIwIiwiMjAyMCIsMSwiIiwiIl0sWyIyMDE5IiwiMjAxOSIsMSwiIiwiIl0sWyIyMDE4IiwiMjAxOCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsiMjAxOSJdfSwiUGFuZWwxX2N0bDAwX1NDX1NoZW5nWUQiOnsiRl9JdGVtcyI6W1si5YyX5LqsIiwi5YyX5LqsIiwxLCIiLCIiXSxbIuays+WMlyIsIuays+WMlyIsMSwiIiwiIl0sWyLlsbHopb8iLCLlsbHopb8iLDEsIiIsIiJdLFsi5YaF6JKZ5Y+kIiwi5YaF6JKZ5Y+kIiwxLCIiLCIiXSxbIui+veWugSIsIui+veWugSIsMSwiIiwiIl0sWyLlkInmnpciLCLlkInmnpciLDEsIiIsIiJdLFsi6buR6b6Z5rGfIiwi6buR6b6Z5rGfIiwxLCIiLCIiXSxbIuS4iua1tyIsIuS4iua1tyIsMSwiIiwiIl0sWyLmsZ/oi48iLCLmsZ/oi48iLDEsIiIsIiJdLFsi5rWZ5rGfIiwi5rWZ5rGfIiwxLCIiLCIiXSxbIuWuieW+vSIsIuWuieW+vSIsMSwiIiwiIl0sWyLnpo/lu7oiLCLnpo/lu7oiLDEsIiIsIiJdLFsi5rGf6KW/Iiwi5rGf6KW/IiwxLCIiLCIiXSxbIuWxseS4nCIsIuWxseS4nCIsMSwiIiwiIl0sWyLmsrPljZciLCLmsrPljZciLDEsIiIsIiJdLFsi5rmW5YyXIiwi5rmW5YyXIiwxLCIiLCIiXSxbIua5luWNlyIsIua5luWNlyIsMSwiIiwiIl0sWyLlub/kuJwiLCLlub/kuJwiLDEsIiIsIiJdLFsi5bm/6KW/Iiwi5bm/6KW/IiwxLCIiLCIiXSxbIumHjeW6hiIsIumHjeW6hiIsMSwiIiwiIl0sWyLlm5vlt50iLCLlm5vlt50iLDEsIiIsIiJdLFsi6LS15beeIiwi6LS15beeIiwxLCIiLCIiXSxbIuS6keWNlyIsIuS6keWNlyIsMSwiIiwiIl0sWyLopb/ol48iLCLopb/ol48iLDEsIiIsIiJdLFsi6ZmV6KW/Iiwi6ZmV6KW/IiwxLCIiLCIiXSxbIueUmOiCgyIsIueUmOiCgyIsMSwiIiwiIl0sWyLpnZLmtbciLCLpnZLmtbciLDEsIiIsIiJdLFsi5paw55aGIiwi5paw55aGIiwxLCIiLCIiXSxbIuWPsOa5viIsIuWPsOa5viIsMSwiIiwiIl0sWyLpppnmuK8iLCLpppnmuK8iLDEsIiIsIiJdLFsi5r6z6ZeoIiwi5r6z6ZeoIiwxLCIiLCIiXSxbIua4r+a+s+WPsCIsIua4r+a+s+WPsCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5rKz5YyXIl19LCJQYW5lbDFfY3RsMDBfU0NfTGVpWGluZyI6eyJGX0l0ZW1zIjpbWyLkuIDmnKwiLCLkuIDmnKwiLDEsIiIsIiJdLFsi6Im65pyv57G7Iiwi6Im65pyv57G7IiwxLCIiLCIiXSxbIuWbveWutuS4k+mhuSIsIuWbveWutuS4k+mhuSIsMSwiIiwiIl0sWyLpq5jmoKHkuJPpobkiLCLpq5jmoKHkuJPpobkiLDEsIiIsIiJdLFsi57u85ZCI6K+E5Lu3Iiwi57u85ZCI6K+E5Lu3IiwxLCIiLCIiXSxbIuS/nemAgeeUnyIsIuS/nemAgeeUnyIsMSwiIiwiIl0sWyLlnLDmlrnkuJPpobkiLCLlnLDmlrnkuJPpobkiLDEsIiIsIiJdLFsi6auY5rC05bmz6L+Q5Yqo5ZGYIiwi6auY5rC05bmz6L+Q5Yqo5ZGYIiwxLCIiLCIiXSxbIuaYpeWto+aLm+eUnyIsIuaYpeWto+aLm+eUnyIsMSwiIiwiIl0sWyLmsJHml4/pooTnp5EiLCLmsJHml4/pooTnp5EiLDEsIiIsIiJdLFsi5a6a5ZCRIiwi5a6a5ZCRIiwxLCIiLCIiXSxbIuWNl+eWhuWNleWIlyIsIuWNl+eWhuWNleWIlyIsMSwiIiwiIl0sWyLkuIDmnKzkuK3lpJYiLCLkuIDmnKzkuK3lpJYiLDEsIiIsIiJdLFsi6aaZ5riv5YWN6K+V55SfIiwi6aaZ5riv5YWN6K+V55SfIiwxLCIiLCIiXSxbIuWumuWQkeWWgOS7gCIsIuWumuWQkeWWgOS7gCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5LiA5pysIl19LCJQYW5lbDFfY3RsMDBfU0NfS2VNWiI6eyJGX0l0ZW1zIjpbWyLlhajpg6giLCLlhajpg6giLDEsIiIsIiJdLFsi5paHIiwi5paHIiwxLCIiLCIiXSxbIueQhiIsIueQhiIsMSwiIiwiIl0sWyLkuI3ljLrliIbmlofnkIYiLCLkuI3ljLrliIbmlofnkIYiLDEsIiIsIiJdLFsi5LiN6ZmQIiwi5LiN6ZmQIiwxLCIiLCIiXSxbIueJqeWMliIsIueJqeWMliIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5YWo6YOoIl19LCJQYW5lbDFfR3JpZDEiOnsiRl9Sb3dzIjpbeyJmMCI6WyLmlociLCLnpL7ljLrlrabpmaIiLCLkurrmlofnpL7np5HnsbsiLCI1NDkiLCI2MTUiLCI2MzAuMiJdLCJmMSI6WzM0OF0sImY2IjoiZnJvdzAifSx7ImYwIjpbIuaWhyIsIuWkluWbveivreWtpumZoiIsIuiLseivrSIsIjU0OSIsIjU4OCIsIjU5NC4zIl0sImYxIjpbMzQ5XSwiZjYiOiJmcm93MSJ9LHsiZjAiOlsi55CGIiwi6ZKx5Lyf6ZW/5a2m6ZmiIiwi55CG56eR6K+V6aqM54+tIiwiNTAyIiwiNjMyIiwiNjM1LjIiXSwiZjEiOlszNTBdLCJmNiI6ImZyb3cyIn0seyJmMCI6WyLnkIYiLCLnpL7ljLrlrabpmaIiLCLnu4/mtY7nrqHnkIbnsbsiLCI1MDIiLCI2MjYiLCI2MjkuMSJdLCJmMSI6WzM1MV0sImY2IjoiZnJvdzMifSx7ImYwIjpbIueQhiIsIuekvuWMuuWtpumZoiIsIueQhuWtpuW3peWtpuexuyIsIjUwMiIsIjYyNyIsIjYyOC42Il0sImYxIjpbMzUyXSwiZjYiOiJmcm93NCJ9LHsiZjAiOlsi55CGIiwi6YCa5L+h5LiO5L+h5oGv5bel56iL5a2m6ZmiIiwi55S15a2Q5L+h5oGv5bel56iLKOWNk+i2iuW3peeoi+W4iOePrSkiLCI1MDIiLCI2MjciLCI2MjkuMyJdLCJmMSI6WzM1M10sImY2IjoiZnJvdzUifSx7ImYwIjpbIueQhiIsIumAmuS/oeS4juS/oeaBr+W3peeoi+WtpumZoiIsIumAmuS/oeW3peeoiyIsIjUwMiIsIjYyNyIsIjYyOC40Il0sImYxIjpbMzU0XSwiZjYiOiJmcm93NiJ9LHsiZjAiOlsi55CGIiwi5Lit5qyn5bel56iL5oqA5pyv5a2m6ZmiIiwi5p2Q5paZ56eR5a2m5LiO5bel56iLIiwiNTAyIiwiNjAyIiwiNjAyLjQiXSwiZjEiOls0OThdLCJmNiI6ImZyb3c3In0seyJmMCI6WyLnkIYiLCLkuK3mrKflt6XnqIvmioDmnK/lrabpmaIiLCLmnLrmorDlt6XnqIsiLCI1MDIiLCI2MDMiLCI2MDcuNiJdLCJmMSI6WzQ5OV0sImY2IjoiZnJvdzgifSx7ImYwIjpbIueQhiIsIuS4reasp+W3peeoi+aKgOacr+WtpumZoiIsIuS/oeaBr+W3peeoiyIsIjUwMiIsIjYwNCIsIjYwOC45Il0sImYxIjpbNTAwXSwiZjYiOiJmcm93OSJ9XSwiUmVjb3JkQ291bnQiOjEwLCJTZWxlY3RlZFJvd0lEQXJyYXkiOltdLCJTZWxlY3RlZENlbGwiOltdfX0='
    }

for year in years[:2]: # 遍历每年每个省份的录取信息
    for province in provinces:
        data1['Panel1$ctl00$SC_Year$Value'] = year
        data1['Panel1$ctl00$SC_Year'] = year
        data1['Panel1$ctl00$SC_ShengYD$Value'] = province
        data1['Panel1$ctl00$SC_ShengYD'] = province       
        
        response = requests.post(url1,data=data1,headers=headers1)
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # 处理数据
        inforStr = str(soup.find_all('script')[-1]) # 包含录取信息的字符串
        inforList = eval((inforStr.split("var f1_state={\"F_Rows\":")[1]).split(",\"RecordCount")[0]) # 包含录取信息的列表
        if(len(inforList) > 0):
            for item in inforList:       
                print(item)
                if(province == '上海' or province == '浙江'):
                    line = ["上海大学", year, province, 'all', item['f0'][2], item['f0'][4], "09118135王屹之"]
                    csv_writer.writerow(line)
                else:
                    line = ["上海大学", year, province, item['f0'][0]+'科', item['f0'][2], item['f0'][4], "09118135王屹之"]
                    csv_writer.writerow(line)

# 第二部分的信息爬取（2016-2017）
"""
上海大学的历年分数网站突然崩了(;_;)，2016-2017年的信息还未爬到，
这两天我会一直关注，网站能访问了我立刻完善后连同数据一并提交！
"""

url2 = 'http://bks.shu.edu.cn/pub/ScoresOld.aspx'

headers2 = {
    'User-agent': random.choice(USER_AGENTS), 
    'Cookie': 'ASP.NET_SessionId=gja4btcx1ffu5wk4yllvtrwx',
    'Connection': 'keep-alive',
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'bks.shu.edu.cn',
    'Referer': 'http://bks.shu.edu.cn/pub/ScoresOld.aspx'
    }

data2 = {
    '__EVENTTARGET':'Panel1$ctl00$btnOK',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'/wEPDwUJLTQxNTE4OTQ4ZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBwUGUGFuZWwxBRRQYW5lbDEkY3RsMDAkU0NfWWVhcgUXUGFuZWwxJGN0bDAwJFNDX1NoZW5nWUQFF1BhbmVsMSRjdGwwMCRTQ19MZWlYaW5nBRRQYW5lbDEkY3RsMDAkU0NfS2VNWgUSUGFuZWwxJGN0bDAwJGJ0bk9LBQxQYW5lbDEkR3JpZDEFDFBhbmVsMSRHcmlkMQ8PZGVkQVC7R1A+7ftRxnMGX/Xac1cPEaVn/wb4nVmpSK4WlHo=',
    '__VIEWSTATEGENERATOR':'44F706D6',
    'Panel1$ctl00$SC_Year$Value':0, # year
    'Panel1$ctl00$SC_Year':0, # year
    'Panel1$ctl00$SC_ShengYD$Value':'', # province
    'Panel1$ctl00$SC_ShengYD':'', # province
    'Panel1$ctl00$SC_LeiXing$Value':'一本',
    'Panel1$ctl00$SC_LeiXing':'一本',
    'Panel1$ctl00$SC_KeMZ$Value':'全部',
    'Panel1$ctl00$SC_KeMZ':'全部',
    'F_TARGET':'Panel1_ctl00_btnOK',
    'Panel1_Grid1_Collapsed':'false',
    'Panel1_Collapsed':'false',
    'F_STATE':'eyJQYW5lbDFfY3RsMDBfU0NfWWVhciI6eyJGX0l0ZW1zIjpbWyIyMDIwIiwiMjAyMCIsMSwiIiwiIl0sWyIyMDE5IiwiMjAxOSIsMSwiIiwiIl0sWyIyMDE4IiwiMjAxOCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsiMjAxOSJdfSwiUGFuZWwxX2N0bDAwX1NDX1NoZW5nWUQiOnsiRl9JdGVtcyI6W1si5YyX5LqsIiwi5YyX5LqsIiwxLCIiLCIiXSxbIuays+WMlyIsIuays+WMlyIsMSwiIiwiIl0sWyLlsbHopb8iLCLlsbHopb8iLDEsIiIsIiJdLFsi5YaF6JKZ5Y+kIiwi5YaF6JKZ5Y+kIiwxLCIiLCIiXSxbIui+veWugSIsIui+veWugSIsMSwiIiwiIl0sWyLlkInmnpciLCLlkInmnpciLDEsIiIsIiJdLFsi6buR6b6Z5rGfIiwi6buR6b6Z5rGfIiwxLCIiLCIiXSxbIuS4iua1tyIsIuS4iua1tyIsMSwiIiwiIl0sWyLmsZ/oi48iLCLmsZ/oi48iLDEsIiIsIiJdLFsi5rWZ5rGfIiwi5rWZ5rGfIiwxLCIiLCIiXSxbIuWuieW+vSIsIuWuieW+vSIsMSwiIiwiIl0sWyLnpo/lu7oiLCLnpo/lu7oiLDEsIiIsIiJdLFsi5rGf6KW/Iiwi5rGf6KW/IiwxLCIiLCIiXSxbIuWxseS4nCIsIuWxseS4nCIsMSwiIiwiIl0sWyLmsrPljZciLCLmsrPljZciLDEsIiIsIiJdLFsi5rmW5YyXIiwi5rmW5YyXIiwxLCIiLCIiXSxbIua5luWNlyIsIua5luWNlyIsMSwiIiwiIl0sWyLlub/kuJwiLCLlub/kuJwiLDEsIiIsIiJdLFsi5bm/6KW/Iiwi5bm/6KW/IiwxLCIiLCIiXSxbIumHjeW6hiIsIumHjeW6hiIsMSwiIiwiIl0sWyLlm5vlt50iLCLlm5vlt50iLDEsIiIsIiJdLFsi6LS15beeIiwi6LS15beeIiwxLCIiLCIiXSxbIuS6keWNlyIsIuS6keWNlyIsMSwiIiwiIl0sWyLopb/ol48iLCLopb/ol48iLDEsIiIsIiJdLFsi6ZmV6KW/Iiwi6ZmV6KW/IiwxLCIiLCIiXSxbIueUmOiCgyIsIueUmOiCgyIsMSwiIiwiIl0sWyLpnZLmtbciLCLpnZLmtbciLDEsIiIsIiJdLFsi5paw55aGIiwi5paw55aGIiwxLCIiLCIiXSxbIuWPsOa5viIsIuWPsOa5viIsMSwiIiwiIl0sWyLpppnmuK8iLCLpppnmuK8iLDEsIiIsIiJdLFsi5r6z6ZeoIiwi5r6z6ZeoIiwxLCIiLCIiXSxbIua4r+a+s+WPsCIsIua4r+a+s+WPsCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5rKz5YyXIl19LCJQYW5lbDFfY3RsMDBfU0NfTGVpWGluZyI6eyJGX0l0ZW1zIjpbWyLkuIDmnKwiLCLkuIDmnKwiLDEsIiIsIiJdLFsi6Im65pyv57G7Iiwi6Im65pyv57G7IiwxLCIiLCIiXSxbIuWbveWutuS4k+mhuSIsIuWbveWutuS4k+mhuSIsMSwiIiwiIl0sWyLpq5jmoKHkuJPpobkiLCLpq5jmoKHkuJPpobkiLDEsIiIsIiJdLFsi57u85ZCI6K+E5Lu3Iiwi57u85ZCI6K+E5Lu3IiwxLCIiLCIiXSxbIuS/nemAgeeUnyIsIuS/nemAgeeUnyIsMSwiIiwiIl0sWyLlnLDmlrnkuJPpobkiLCLlnLDmlrnkuJPpobkiLDEsIiIsIiJdLFsi6auY5rC05bmz6L+Q5Yqo5ZGYIiwi6auY5rC05bmz6L+Q5Yqo5ZGYIiwxLCIiLCIiXSxbIuaYpeWto+aLm+eUnyIsIuaYpeWto+aLm+eUnyIsMSwiIiwiIl0sWyLmsJHml4/pooTnp5EiLCLmsJHml4/pooTnp5EiLDEsIiIsIiJdLFsi5a6a5ZCRIiwi5a6a5ZCRIiwxLCIiLCIiXSxbIuWNl+eWhuWNleWIlyIsIuWNl+eWhuWNleWIlyIsMSwiIiwiIl0sWyLkuIDmnKzkuK3lpJYiLCLkuIDmnKzkuK3lpJYiLDEsIiIsIiJdLFsi6aaZ5riv5YWN6K+V55SfIiwi6aaZ5riv5YWN6K+V55SfIiwxLCIiLCIiXSxbIuWumuWQkeWWgOS7gCIsIuWumuWQkeWWgOS7gCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5LiA5pysIl19LCJQYW5lbDFfY3RsMDBfU0NfS2VNWiI6eyJGX0l0ZW1zIjpbWyLlhajpg6giLCLlhajpg6giLDEsIiIsIiJdLFsi5paHIiwi5paHIiwxLCIiLCIiXSxbIueQhiIsIueQhiIsMSwiIiwiIl0sWyLkuI3ljLrliIbmlofnkIYiLCLkuI3ljLrliIbmlofnkIYiLDEsIiIsIiJdLFsi5LiN6ZmQIiwi5LiN6ZmQIiwxLCIiLCIiXSxbIueJqeWMliIsIueJqeWMliIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5YWo6YOoIl19LCJQYW5lbDFfR3JpZDEiOnsiRl9Sb3dzIjpbeyJmMCI6WyLmlociLCLnpL7ljLrlrabpmaIiLCLkurrmlofnpL7np5HnsbsiLCI1NDkiLCI2MTUiLCI2MzAuMiJdLCJmMSI6WzM0OF0sImY2IjoiZnJvdzAifSx7ImYwIjpbIuaWhyIsIuWkluWbveivreWtpumZoiIsIuiLseivrSIsIjU0OSIsIjU4OCIsIjU5NC4zIl0sImYxIjpbMzQ5XSwiZjYiOiJmcm93MSJ9LHsiZjAiOlsi55CGIiwi6ZKx5Lyf6ZW/5a2m6ZmiIiwi55CG56eR6K+V6aqM54+tIiwiNTAyIiwiNjMyIiwiNjM1LjIiXSwiZjEiOlszNTBdLCJmNiI6ImZyb3cyIn0seyJmMCI6WyLnkIYiLCLnpL7ljLrlrabpmaIiLCLnu4/mtY7nrqHnkIbnsbsiLCI1MDIiLCI2MjYiLCI2MjkuMSJdLCJmMSI6WzM1MV0sImY2IjoiZnJvdzMifSx7ImYwIjpbIueQhiIsIuekvuWMuuWtpumZoiIsIueQhuWtpuW3peWtpuexuyIsIjUwMiIsIjYyNyIsIjYyOC42Il0sImYxIjpbMzUyXSwiZjYiOiJmcm93NCJ9LHsiZjAiOlsi55CGIiwi6YCa5L+h5LiO5L+h5oGv5bel56iL5a2m6ZmiIiwi55S15a2Q5L+h5oGv5bel56iLKOWNk+i2iuW3peeoi+W4iOePrSkiLCI1MDIiLCI2MjciLCI2MjkuMyJdLCJmMSI6WzM1M10sImY2IjoiZnJvdzUifSx7ImYwIjpbIueQhiIsIumAmuS/oeS4juS/oeaBr+W3peeoi+WtpumZoiIsIumAmuS/oeW3peeoiyIsIjUwMiIsIjYyNyIsIjYyOC40Il0sImYxIjpbMzU0XSwiZjYiOiJmcm93NiJ9LHsiZjAiOlsi55CGIiwi5Lit5qyn5bel56iL5oqA5pyv5a2m6ZmiIiwi5p2Q5paZ56eR5a2m5LiO5bel56iLIiwiNTAyIiwiNjAyIiwiNjAyLjQiXSwiZjEiOls0OThdLCJmNiI6ImZyb3c3In0seyJmMCI6WyLnkIYiLCLkuK3mrKflt6XnqIvmioDmnK/lrabpmaIiLCLmnLrmorDlt6XnqIsiLCI1MDIiLCI2MDMiLCI2MDcuNiJdLCJmMSI6WzQ5OV0sImY2IjoiZnJvdzgifSx7ImYwIjpbIueQhiIsIuS4reasp+W3peeoi+aKgOacr+WtpumZoiIsIuS/oeaBr+W3peeoiyIsIjUwMiIsIjYwNCIsIjYwOC45Il0sImYxIjpbNTAwXSwiZjYiOiJmcm93OSJ9XSwiUmVjb3JkQ291bnQiOjEwLCJTZWxlY3RlZFJvd0lEQXJyYXkiOltdLCJTZWxlY3RlZENlbGwiOltdfX0='
    }

for year in years[2:]: # 遍历每年每个省份的录取信息
    for province in provinces:
        
        data2['Panel1$ctl00$SC_Year$Value'] = year,
        data2['Panel1$ctl00$SC_Year'] = year,
        data2['Panel1$ctl00$SC_ShengYD$Value'] = province,
        data2['Panel1$ctl00$SC_ShengYD'] = province,

        response = requests.post(url2,data=data2,headers=headers2)
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # 处理数据
        inforStr = str(soup.find_all('script')[-1]) # 包含录取信息的字符串
        inforList = eval((inforStr.split("RecordCount\":6,\"F_Rows\":")[1].split("};var f10_columns")[0]).replace('null', '')) # 包含录取信息的列表
        if(len(inforList) > 0):  
            for item in inforList:       
                print(item)
                # 分别提取文科和理科最低分
                if(len(item['f0'][1]) != 0):
                    line = ["上海大学", year, province, '文科', item['f0'][0], item['f0'][1], "09118135王屹之"]
                    csv_writer.writerow(line)
                if(len(item['f0'][2]) != 0):
                    line = ["上海大学", year, province, '理科', item['f0'][0], item['f0'][2], "09118135王屹之"]
                    csv_writer.writerow(line)
            
# 关闭文件 
file.close()
    