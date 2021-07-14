import requests as r
import json
import csv

url = 'https://lqcx.buaa.edu.cn/f/ajax_lnfs'

pro_str='北京 天津 河北 山西 内蒙古 辽宁 吉林 黑龙江 上海 江苏 浙江 安徽 福建 江西 山东 河南 湖北 湖南 广东 广西 海南 重庆 四川 贵州 云南 西藏 陕西 甘肃 青海 宁夏 新疆 台湾 香港 澳门'
provinces = pro_str.split(' ')

years = [2019,2018]
categories = ['理工','文史']

headers={
	'Cookie': 'zhaosheng.buaa.session.id=7d490af9431d4465bb753fec74553d6d',
	'Host': 'lqcx.buaa.edu.cn',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

head = ['College','Year','Province','Category','Major','Score','Contributor']
f = open('09118106 戴恒洁-北京航空航天大学.csv','at',encoding='utf-8-sig',newline='')
writer = csv.writer(f)
writer.writerow(head)

for year in years:
	for province in provinces:
		for category in categories:
			payload = {
				'ssmc': province,
				'zsnf': year,
				'klmc': category,
				'zslx': '统招'
			}
	
			res = r.post(url=url,data=payload,headers=headers)
			print(res.status_code)
			
			res.encoding = res.apparent_encoding
			data = json.loads(res.text)

			if 'data' in data.keys():
				for item in data['data']['sszygradeList']:
					lst = ['北京航空航天大学',year,province,category]
					if item['zymc']:
						lst.append(item['zymc'])
					if item['minScore']:
						lst.append(item['minScore'])
						lst.append('09118106-戴恒洁')
					f = open('09118106 戴恒洁-北京航空航天大学.csv','at',encoding='utf-8-sig',newline='')
					writer = csv.writer(f)
					writer.writerow(lst)

