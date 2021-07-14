import requests
from bs4 import BeautifulSoup
import csv
def check_link(year):
    try:
        url = 'http://hqg.ybu.edu.cn/zs/ajax.php?act=pcchange'
        # 设置url post请求的参数
        data = {'nf': year}
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': '*/*', 'Accept-Language': 'zh-cn', 'Accept-Encoding': 'gzip, deflate',
                   'Host': 'hqg.ybu.edu.cn', 'Origin': 'http://hqg.ybu.edu.cn',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
                   'Connection': 'keep-alive', 'Referer': 'http://hqg.ybu.edu.cn/zs/lnfs.php?nf=2018&sf=&kl=&pc=&mz=',
                   'Content-Length': '19', 'Cookie': 'PHPSESSID=394bcac35edbf38e3deb74b34dbe0d45',
                   'X-Requested-With': 'XMLHttpRequest'}
        req = requests.post(url, data=data, headers=headers)
        req.encoding = 'utf-8'
        return req.text
    except:
        print('无法链接服务器')

def get_contents(rurl):
    soup = BeautifulSoup(rurl, 'html.parser')
    # print(soup.table.tr.td.contents)
    data_list = []
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:  # 忽略表头，其实是冗余的，因为下面要筛选'一批'
            tds = tr.find_all('td')
            if tds[5].contents[0] == '一批':

                if tds[4].contents[0] == '理工':
                    data_list.append({
                        'College': '延边大学',
                        'Year': tds[1].contents[0],
                        'Province': tds[2].contents[0],
                        'Category': '理科',
                        'Major': tds[7].contents[0],
                        'Score': tds[9].string,
                        'Contributor': '09118209祁丁然'
                    })
                elif tds[4].contents[0] == '文史':
                    data_list.append({
                        'College': '延边大学',
                        'Year': tds[1].contents[0],
                        'Province': tds[2].contents[0],
                        'Category': '文科',
                        'Major': tds[7].contents[0],
                        'Score': tds[9].string,
                        'Contributor': '09118209祁丁然'
                    })
                else:
                    data_list.append({
                        'College': '延边大学',
                        'Year': tds[1].contents[0],
                        'Province': tds[2].contents[0],
                        'Category': 'all',
                        'Major': tds[7].contents[0],
                        'Score': tds[9].string,
                        'Contributor': '09118209祁丁然'
                    })


    print(data_list)
    return data_list

def save_csv(data_list):
    with open("09118209祁丁然-延边大学.csv", "a+", newline='') as csvfile:
        writer = csv.writer(csvfile)
        #以读的方式打开csv 用csv.reader方式判断是否存在标题。
        with open("09118209祁丁然-延边大学.csv", "r", newline="") as f:
            reader = csv.reader(f)
            #多次读写，判断是否需要加表头
            if not [row for row in reader]:
                writer.writerow(data_list[0].keys())
                for i in data_list:
                    writer.writerow(i.values())
            else:
                for i in data_list:
                    writer.writerow(i.values())


if __name__=='__main__':
    #运行一次即可，运行多次会导致数据重复，2次运行应删去原文件
    save_csv(get_contents(check_link('2016')))
    save_csv(get_contents(check_link('2017')))
    save_csv(get_contents(check_link('2018')))
    save_csv(get_contents(check_link('2019')))