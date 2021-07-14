import requests
from bs4 import BeautifulSoup
import csv


# 爬取相关数据
def get_html(url, times):
    # 获取html信息并找到相关标签
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    tables = soup.select('div ~ table', class_='panel-heading')
    # 获取专业及分数等数据
    for index, table in enumerate(tables):
        tr = table.find_all('tr')
        for j in tr:
            td = j.select('td')
            score_list = ['西南财经大学', year[times]]
            for k in td:
                if 'class' not in k.attrs:
                    score = k.text.strip()
                    score_list.append(score)
            score_detail.append(score_list)


# 获取所有页面的url
def all_page():
    # 找规律
    base_url_trade = 'http://zscx.swufe.edu.cn/resume/resume-list.php?key=&jobcategory=&trade='
    base_url_citycategory = '&citycategory='
    base_url_education = '&major=&experience=75&resumetag=&education='
    base_url = '&sex=&photo=&talent=&settr=&page=1'
    urllist = []
    citycategory_list = [i for i in range(1,32)]
    citycategory_list.append(538)
    '''
    遍历获取所有url
    trade对应年份2019，2018，2017
    citycategory对应省份
    education对应理工科，文史和综合改革
    '''
    for trade in [312,298,294]:
        for citycategory in citycategory_list:
            for education in [65,66,67]:
                allurl = base_url_trade + str(trade) + base_url_citycategory + str(citycategory) + base_url_education \
                     + str(education) + base_url
                urllist.append(allurl)
    return urllist


# 解析页面并按要求返回列表
def html_parse():
    times = 0
    for url in all_page():
        get_html(url, times)
        times = times + 1
    score = []
    '''
    部分年份部分省份信息缺失
    删除列表中对应元素
    例如2019年浙江省无理工科和文史科
    '''
    for i in score_detail:
        if len(i) <= 2:
            score_detail.remove(i)
    # 将列表元素转为['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor']顺序
    for i in score_detail:
        score.append([i[0], i[1], i[5], i[4], i[2], i[6], '61518309羊宇培'])
    return score


if __name__ == '__main__':
    score_detail = []
    year = ['2019', '2018', '2017']
    year = [val for val in year for i in range(96)]
    score = html_parse()
    name_attribute = ['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor']
    # 保存为csv文件
    csvFile = open('./61518309羊宇培-西南财经大学.csv', "w+", newline='')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(name_attribute)
        for i in range(len(score)):
            writer.writerow(score[i])
    finally:
        csvFile.close()
        print('爬完了！')
