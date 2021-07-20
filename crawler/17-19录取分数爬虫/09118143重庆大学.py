# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:41:34 2020

@author: Ryan He
"""


import requests
from bs4 import BeautifulSoup
import csv

def get_years_provinces(url):
    """
    从录取分数线查询页面获取可查询的所有年份和省份
    """
    years_list = []  # 存放年份
    provinces_list = []  # 存放省份
    # 用get方法获取页面信息
    r = requests.get(url)
    # 转化为BeautifulSoup对象, 解析页面
    htmlcontent=r.content.decode('utf-8')
    bs = BeautifulSoup(htmlcontent,'lxml')
    # 查找年份和省份数据
    years = bs.find(id = 'year')
    years = years.find_all('a')
    provinces = bs.find(id = 'province')
    provinces = provinces.find_all('a')
    
    for year in years:
        years_list.append(year.text)
    for province in provinces:
        provinces_list.append(province.text)
    
    return years_list, provinces_list
    
def get_benchmark(url, data, header):
    """
    post某一年份某一省份的录取分数线数据
    """
    benchmark = []  # 格式化存储录取分数线数据
    # 用post方法获取页面信息
    r = requests.post(url, data=data, headers=header)
    # 转化为BeautifulSoup对象, 解析页面
    htmlcontent=r.content.decode('utf-8')
    bs = BeautifulSoup(htmlcontent,'lxml')
    # 将数据按行分离
    all_tr =bs.find_all('tr')
    
    for tr in all_tr:
        # 将每一行的元素分离
        all_td = tr.find_all('td')
        # 剔除不符合条件的数据(非本科一批普通类)
        if (all_td[1].text not in ['普通类', '本科一批普通类']) or all_td[2].text in ['理工民', '文史民']:
            continue
        # 将数据按预定格式存储
        row = ['重庆大学', data['year'], data['province']]
        if all_td[2].text in ['理工', '理工汉']:
            row.append('理科')
        elif all_td[2].text in ['文史', '文史汉']:
            row.append('文科')
        else:
            row.append('all')
        row.append(all_td[5].text)
        row.append(all_td[6].text)
        row.append('09118143何洋龙')
        benchmark.append((row))
        
    return benchmark
        
def get_all_benchmark(url, provinces, years, header):
    """
    获取所有可查询年份和省份的录取分数线数据
    """
    all_benchmark = []  # 存储所有可查询省份和年份的数据
    data = {}
    # 遍历所有省份和年份
    for province in provinces:
        data['province'] = province
        for year in years:
            data['year'] = year
            print('获取'+year+province+'数据中...')
            benchmark = get_benchmark(url, data, header)
            all_benchmark.append(benchmark)
            
    return all_benchmark

url1 = 'http://zhaosheng.cqu.edu.cn/Home/queryLqfs/23' # 分数查询页面URL, 用于获取各个省份和年份
url2 = 'http://zhaosheng.cqu.edu.cn/WebApi/FrontManager/GetLqfsData' # 各专业录取分数线URL
header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '37',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'safedog-flow-item=',
    'Host': 'zhaosheng.cqu.edu.cn',
    'Origin': 'http://zhaosheng.cqu.edu.cn',
    'Referer': 'http://zhaosheng.cqu.edu.cn/Home/queryLqfs/23',
    'User-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'X-Requested-With': 'XMLHttpRequest'}
data = {} # 传入post方法的参数, 包含年份'year', 省份'province'

years, provinces = get_years_provinces(url1)  # 获取可查询的所有年份和省份
benchmark_data = get_all_benchmark(url2, provinces, years, header)  #获取所有录取分数线数据
# 将数据按预定格式保存为.csv文件(newline=''防止文件中出现空行)
with open('09118143何洋龙-重庆大学.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['College', 'Year', 'Province', 'Category',
                    'Major', 'Score', 'Contributor'])
    for benchmark in benchmark_data:
        f_csv.writerows(benchmark)
    