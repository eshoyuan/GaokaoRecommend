import requests
import pandas as pd
import csv

# 用于遍历的列表
province_list = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建',
                 '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏',
                 '陕西', '甘肃', '青海', '宁夏', '新疆', '新疆内地班', '西藏内地班', '港澳台侨联招']
year_list = ['2019', '2018', '2017']

# 爬虫的header
header1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
              image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'Keep-Alive',
    'Host': 'wsbm.ecust.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}


def request_url(url, data1):
    try:
        response = requests.post(url, data=data1, headers=header1)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def main(province, year):
    data1 = {
        'province': province,
        'nf': year,
    }  # 对页面的动态申请
    url = 'https://wsbm.ecust.edu.cn/lqfs.htm'
    html = request_url(url, data1)
    df = pd.read_html(html)  # 使用pandas的html解析功能对表格进行解析
    table = df[6]  # 选择我们要处理的表
    print(table)
    for ii in range(2, table.shape[0]):
        csv_writer.writerow(["华东理工大学", year, province, table[4][ii], table[6][ii], table[9][ii], "09118138朱浩鹏"])


if __name__ == '__main__':
    f = open('09118138朱浩鹏-华东理工大学.csv', 'w', newline='', encoding='ANSI')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["College", "Year", "Province", "Category", "Major", "Score", "Contributor"])
    for i in province_list:
        for j in year_list:
            main(i, j)
