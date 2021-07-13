# syy crawler
import json
import requests
import random
import urllib.parse
import pandas as pd
import os

year = '2020'
province = '河北'
batchNames = ['本科批', '本科提前批']
universities = ['清华大学', '北京大学', '复旦大学', '中国人民大学', '上海交通大学',
                '浙江大学', '中国科学技术大学', '南京大学', '同济大学', '哈尔滨工业大学', '西安交通大学', '北京航空航天大学',
                '天津大学', '华中科技大学', '东南大学', '南开大学', '中山大学', '武汉大学', '厦门大学',
                '北京师范大学', '国防科学技术大学', '吉林大学', '四川大学', '湖南大学', '山东大学', '中南大学',
                '华南理工大学', '北京理工大学', '大连理工大学', '西北工业大学', '重庆大学', '电子科技大学', '兰州大学',
                '东北大学', '华东师范大学', '中国农业大学', '中国海洋大学', '西北农林科技大学', '中央民族大学']  # 这里目前只录入985院校


def get_text(university=0, batchName=0):
    """获取网页文本信息"""
    university_url = urllib.parse.quote(universities[university])
    batchName_url = urllib.parse.quote(batchNames[batchName])
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
        'province': '%E6%B2%B3%E5%8C%97',
        'rn': '10',
        'school': university_url,
        'sortType': '',
        'year': year,
    }
    textUrl = 'https://gaokao.baidu.com/gaokao/gkschool/majorscore?ajax=1&batchName={}&curriculum=&needFilter=0&pn=1&province=%E6%B2%B3%E5%8C%97&rn=50&school={}&sortType=&year=2020'.format(
        batchName_url, university_url)
    try:
        r = requests.post(textUrl, data=data1, headers=headers1, timeout=30)
        r.raise_for_status()  # 如果访问状态码不是200，则抛出异常
        r.encoding = 'utf-8'
        return r.text
    except:
        print("连接失败")


path = '2020.csv'


def get_csv(uname, batch):
    text = get_text(uname, batch)
    dict_text = json.loads(text)
    data = dict_text['data']['majorScore']
    dataList = data['dataList']
    scoreData = []
    for i in dataList:
        university = i['legalName']
        majorName = i['majorName']
        curriculum = i['curriculum']
        batchName = i['batchName']
        minScore = i['minScore']
        minScoreOrder = i['minScoreOrder']
        scoreData.append([university, majorName, minScore, minScoreOrder, curriculum, batchName])
    df = pd.DataFrame(scoreData, columns=['院校', '专业', '最低分', '位次', '科目', '批次'])
    if os.path.exists(path):
        df.to_csv(path, index=False, mode='a', header=None, encoding="gbk")
    else:
        df.to_csv(path, index=False, encoding="gbk")


for i in range(len(universities)):
    for j in range(len(batchNames)):
        get_csv(i, j)
