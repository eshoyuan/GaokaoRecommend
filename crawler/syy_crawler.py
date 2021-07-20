# -*- coding: utf-8 -*-
# syy crawler

import json
import requests
import random
import urllib.parse
import pandas as pd
import os
import re

# 筛选条件
years = ['2016', '2017', '2018', '2019', '2020']
province = '山东'
batchNames = ['本科批', '本科一批', '本科提前批', '普通类一段']

university_985 = ['清华大学', '北京大学', '复旦大学', '中国人民大学', '上海交通大学',
                  '浙江大学', '中国科学技术大学', '南京大学', '同济大学', '哈尔滨工业大学', '西安交通大学', '北京航空航天大学',
                  '天津大学', '华中科技大学', '东南大学', '南开大学', '中山大学', '武汉大学', '厦门大学',
                  '北京师范大学', '国防科学技术大学', '吉林大学', '四川大学', '湖南大学', '山东大学', '中南大学',
                  '华南理工大学', '北京理工大学', '大连理工大学', '西北工业大学', '重庆大学', '电子科技大学', '兰州大学',
                  '东北大学', '华东师范大学', '中国农业大学', '中国海洋大学', '西北农林科技大学', '中央民族大学']  # 985院校

university_211 = [
    '清华大学',
    '北京大学',
    '浙江大学',
    '复旦大学',
    '上海交通大学',
    '南京大学',
    '中国科学技术大学',
    '中国人民大学',
    '武汉大学',
    '中山大学',
    '吉林大学',
    '华中科技大学',
    '天津大学',
    '四川大学',
    '南开大学',
    '北京师范大学',
    '西安交通大学',
    '哈尔滨工业大学',
    '中南大学',
    '山东大学',
    '厦门大学',
    '同济大学',
    '东南大学',
    '北京航空航天大学',
    '东北大学',
    '大连理工大学',
    '华南理工大学',
    '华东师范大学',
    '湖南大学',
    '重庆大学',
    '西北工业大学',
    '中国农业大学',
    '兰州大学',
    '北京理工大学',
    '华中师范大学',
    '西南大学',
    '东北师范大学',
    '南京农业大学',
    '北京交通大学',
    '西南交通大学',
    '长安大学',
    '武汉理工大学',
    '河海大学',
    '南京师范大学',
    '郑州大学',
    '南京理工大学',
    '西安电子科技大学',
    '中国海洋大学',
    '华东理工大学',
    '苏州大学',
    '南京航空航天大学',
    '中国矿业大学',
    '北京科技大学',
    '上海大学',
    '南昌大学',
    '西北农林科技大学',
    '湖南师范大学',
    '云南大学',
    '哈尔滨工程大学',
    '东华大学',
    '华南师范大学',
    '上海财经大学',
    '陕西师范大学',
    '中国政法大学',
    '暨南大学',
    '北京邮电大学',
    '江南大学',
    '合肥工业大学',
    '北京化工大学',
    '中南财经政法大学',
    '中国地质大学',
    '福州大学',
    '西南财经大学',
    '广西大学',
    '北京工业大学',
    '北京林业大学',
    '中央民族大学',
    '华北电力大学',
    '中国人民解放军空军军医大学',
    '中国人民解放军第二军医大学',
    '国防科学技术大学',
    '石河子大学',
    '新疆大学',
    '宁夏大学',
    '青海大学',
    '西北大学',
    '西藏大学',
    '贵州大学',
    '四川农业大学',
    '电子科技大学',
    '海南大学',
    '华南农业大学',
    '华中农业大学',
    '中国石油大学',
    '安徽大学',
    '中国药科大学',
    '上海外国语大学',
    '东北林业大学',
    '东北农业大学',
    '延边大学',
    '大连海事大学',
    '辽宁大学',
    '内蒙古大学',
    '太原理工大学',
    '河北工业大学',
    '天津医科大学',
    '中国地质大学',
    '中国石油大学',
    '中国矿业大学',
    '华北电力大学',
    '中央音乐学院',
    '北京体育大学',
    '对外经济贸易大学',
    '中央财经大学',
    '中国传媒大学',
    '北京外国语大学',
    '北京中医药大学']  # 211院校


def is_985(name):
    if name not in university_985:
        return 0
    else:
        return 1


def is_211(name):
    if name not in university_211:
        return 0
    else:
        return 1


# 读取大学名称列表
universityDir = "./17-19录取分数爬虫"
x = os.listdir(universityDir)
universities = []
for i in x:
    myPattern = re.compile('[\u4e00-\u9fa5]+')
    universities.append(myPattern.findall(i)[0])


# 获取网页文本信息
def get_text(university=0, batchName=0, yearNum=0):
    university_url = urllib.parse.quote(universities[university])
    batchName_url = urllib.parse.quote(batchNames[batchName])
    year_url = urllib.parse.quote(years[yearNum])
    USER_AGENTS = [
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    ]
    headers1 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'BIDUPSID=985327E9DED4E8A875724FFE74A1D32F; PSTM=1620715122; __yjs_duid=1_ca861c7066ee918962fddfec1b805f4f1620716427814; BDUSS=XBMYmVQYVZVU0JQc1NwVzJGUGNwd3JERnNFMVRNSnN6eDhHNHBiejd5QWhNYzlnRVFBQUFBJCQAAAAAAAAAAAEAAABaxNcwc3l5MTIxMzgzOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACGkp2AhpKdga; BDUSS_BFESS=XBMYmVQYVZVU0JQc1NwVzJGUGNwd3JERnNFMVRNSnN6eDhHNHBiejd5QWhNYzlnRVFBQUFBJCQAAAAAAAAAAAEAAABaxNcwc3l5MTIxMzgzOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACGkp2AhpKdga; BAIDUID=90A893A4D138E0F9580E9F173C450220:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID_BFESS=tAFOJeC62ufSzETeNaV8hD2us6dQrw6TH6f3FNbZpcPTC7jWEHupEG0PsU8g0KubxGazogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbu8_DLMfI-3jt-kbn5OKJ3H-UIs-UolB2Q-5KL-bRQ6Jl52bfTH36kJQa5tb55bL6rf_fbdJJL5slrPWR3j0h0djU6U0xvt-gTxoUJbQCnJhhvG-R7n-JIebPRiWTj9QgbLMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjK2jjO03f; BAIDUID_BFESS=90A893A4D138E0F9580E9F173C450220:FG=1',
        'Host': 'gaokao.baidu.com',
        'Referer': 'https://gaokao.baidu.com/gaokao/m/school/score?word={}'.format(university_url),
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-agent': random.choice(USER_AGENTS),
    }
    data1 = {
        'ajax': '1',
        'batchName': batchName_url,
        'curriculum': '',
        'needFilter': '0',
        'pn': '1',
        'province': '%E5%B1%B1%E4%B8%9C',
        'rn': '10',
        'school': university_url,
        'sortType': '',
        'year': year_url,
    }
    textUrl = 'https://gaokao.baidu.com/gaokao/gkschool/majorscore?ajax=1&batchName={}&curriculum=&needFilter=0&pn=1&province=%E5%B1%B1%E4%B8%9C&rn=50&school={}&sortType=&year={}'.format(
        batchName_url, university_url, year_url)
    try:
        r = requests.post(textUrl, data=data1, headers=headers1, timeout=30)
        r.raise_for_status()  # 如果访问状态码不是200，则抛出异常
        r.encoding = 'utf-8'
        return r.text
    except:
        print("连接失败")


# 保存路径设置
path = 'shandong_16-20.csv'


# 解析数据并写入csv文件
def get_csv(uname, batch, year, save_path):
    text = get_text(uname, batch, year)
    dict_text = json.loads(text)
    data = dict_text['data']['majorScore']
    dataList = data['dataList']
    scoreData = []
    for i in dataList:
        university = i['legalName']
        majorNameDesc = i['majorNameDesc']
        simpleMajorName = i['simpleMajorName']
        if year != 4:
            curriculum = i['curriculum']
        else:
            curriculum = i['specialCourse']
        batchName = i['batchName']
        minScore = i['minScore']
        minScoreOrder = i['minScoreOrder']
        yearNum = i['year']
        is985 = is_985(i['legalName'])
        is211 = is_211(i['legalName'])
        if minScore != '':
            scoreData.append(
                [university, simpleMajorName, majorNameDesc, yearNum,
                 minScore, minScoreOrder, curriculum, batchName, is985, is211])
    df = pd.DataFrame(scoreData, columns=['院校', '专业', '专业详情', '年份', '最低分', '位次', '科目', '批次', '985', '211'])
    if os.path.exists(path):
        df.to_csv(save_path, index=False, mode='a', header=None, encoding="utf_8_sig")
    else:
        df.to_csv(save_path, index=False, encoding="utf_8_sig")


# 爬取数据
for i in range(len(universities)):
    for j in range(len(batchNames)):
        for k in range(len(years)):
            get_csv(i, j, k, path)

