# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:49:05 2020

@author: 12921
"""

import requests
with open("./09118105汪铮沁-石河子大学.csv", 'a+') as f:
    f.write('College,Year,Province,Category,Major,Score,Contributor\n')

start_url = 'http://202.201.161.223:8080/Control/QueryInfor.ashx'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://202.201.161.223:8080/Query_Lnlqsj.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

years = ['2019', '2018', '2017']

addresss = [
    '北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海',
    '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南',
    '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西',
    '甘肃', '青海', '宁夏', '新疆', '台湾', '香港', '澳门'
]

for year in years:
    for address in addresss:
        print(f"开始采集：{year} --> {address}")
        post_data = {
            'spannf': year,
            'sfspan': address,
            'keys': '7'
        }
        response = requests.post(start_url, headers=headers, data=post_data)
        js = response.json()
        if 'queryLnlqsjinfor' in js:
            if js['queryLnlqsjinfor'] != []:
                for queryLnlqsjin in js['queryLnlqsjinfor']:
                    item = {}
                    item['school'] = '石河子大学'
                    item['nf'] = queryLnlqsjin['Nf']
                    item['sf'] = queryLnlqsjin['Sf']
                    item['wlk'] = 'all'
                    item['zymc'] = queryLnlqsjin['Zymc'].replace(',', '，')
                    item['bot'] = queryLnlqsjin['Bot']
                    item['Contributer'] = '09118105汪铮沁'
                    print(item)
                    datas = ','.join([str(i) for i in item.values()]) + '\n'
                    with open("./09118105汪铮沁-石河子大学.csv", 'a+') as f:
                        f.write(datas)
            else:
                print(f"未查到：{year} --> {address}")