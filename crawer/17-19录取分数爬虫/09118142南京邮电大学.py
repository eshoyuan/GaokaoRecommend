import requests
import pandas as pd
import csv

year_list = ['2016', '2017', '2018']  # 用于遍历的列表
host_url = 'http://bkzs.nufe.edu.cn/'  # 南京财经大学官网
info = []  # 存储所有分数线信息的列表


def request_url(url, data):
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def spider_1(year):
    '''
    爬取南京财经大学2016至2018年的数据  (2016至2018年的数据是用下拉框进行查询)
    '''
    data = {
        'nf': year,  # 用于搜索的年号
    }
    html = request_url(host_url + 'ldcx.jsp?wbtreeid=1023', data)
    df = pd.read_html(html)  # 使用pandas的read_html函数对表格进行解析
    table = df[0]  # 选择我们需要的表
    for i in range(table.shape[0]):
        province = table['省份'][i]  # 省份
        category = table['科类'][i]  # 科类
        major = table['专业'][i]  # 专业
        min_score = table['最低分'][i]  # 最低分
        sequence = table['批次'][i]  # 批次
        if sequence == '本二':  # 去除本二的数据
            continue
        else:
            if major == '所有':
                major = 'Any'
            info.append(['南京财经大学', year, province, category, major, min_score, '09118142蒋林煊'])


def spider_2():
    '''
    爬取南京财经大学2019年的数据  (2019的数据是在另一个网页上)
    '''
    html = requests.post(host_url + 'info/1007/2232.htm')
    df = pd.read_html(html.content)  # 使用pandas的read_html函数对表格进行解析
    table = df[0]  # 选择我们需要的表
    for i in range(1, table.shape[0]):
        province = table[0][i]  # 省份
        category = table[2][i] + '科'  # 科目
        min_score = table[8][i]  # 最低分
        sequence = table[1][i]  # 批次
        if province == '新疆':  # 筛去新疆很多专项计划
            if sequence == '本一普通':
                info.append(['南京财经大学', 2019, province, category, 'Any', min_score, '09118142蒋林煊'])
            else:
                continue
        elif province == '上海':  # 上海叫组一组二，不叫文理科
            info.append(['南京财经大学', 2019, province, table[2][i], 'Any', min_score, '09118142蒋林煊'])
        else:
            if sequence == '贫困专向':  # 去除本二的数据
                continue
            else:
                info.append(['南京财经大学', 2019, province, category, 'Any', min_score, '09118142蒋林煊'])


if __name__ == '__main__':
    spider_2()
    for i in year_list:
        spider_1(i)
    # 写入csv文件
    with open('09118142蒋林煊-南京财经大学.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['College', 'Year', 'Province', 'Category', 'Major', 'Score', 'Contributor'])
        writer.writerows(info)
