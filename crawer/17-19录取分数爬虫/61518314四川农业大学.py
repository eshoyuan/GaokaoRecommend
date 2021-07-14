import requests
import csv
from bs4 import BeautifulSoup
import re
#因四川农业大学三年数据存储方式更不相同，因此分别对三年数据进行爬取，其中2019年数据表格中存在链接，我对表格中链接数据与非链接数据分别爬取
url_2019 = "http://zs.sicau.edu.cn/?p=16&a=view&r=704"#2019年数据链接
url_2018 = "http://zs.sicau.edu.cn/?p=16&a=view&r=508"#2018年数据链接
url_2017 = "http://zs.sicau.edu.cn/?p=16&a=view&r=385"#2017年数据链接


#2019

def check_link(url):
    '''
    检查url是否可以访问
    :param url: 要访问的url
    :return: 若可以访问则返回url的text内容
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8 '
        return r.text
    except:
        print('无法链接服务器！！！')


def regularization(url):
    '''
    正则化,提取表格中的链接
    :param url: 一段需要提取链接的string
    :return: 返回提取到的链接
    '''
    res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    regular=re.findall(res_url,url,re.I|re.S|re.M)
    regular=regular[0]
    regular=regular.replace('amp;','')#提取到的链接与实际所访问的链接有一定出入，把不需要的部分去掉
    return regular


def get_2019_contents(url_content, response):
    '''
    提取2019年的表格中没有链接的省份信息
    :param url_content: 将获取的表中内容存在url_content中
    :param response: url.text内容
    :return: None
    '''
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find_all('tr')

    for row in table:
        contents=[]#每一行内容
        for element in row:
            if element:
                content=element.string
                if content:#清除字符串里的多余格式
                    content = content.replace('\n', '')
                    content = content.replace('\r', '')
                    content = content.replace('\t', '')
                if content:
                    contents.append(content)
        url_content.append(contents)


def get_links(url_content, response):
    '''
    获取2019年表中的所有链接
    :param url_content: 将获取的表中内容存在url_content中
    :param response: url.text内容
    :return: None
    '''
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find_all('tr')

    for row in table:
        contents=[]
        for element in row:
            if element:
                if element.find('a') != -1 and element.find('a'):
                    res = regularization(str(element.find('a')))#正则化提取网页链接
                    contents.append(res)
        if contents:
            url_content.append(contents[0])


def get_contents_2019(url_content, response):
    '''
    对于在2019表内有链接的用此函数获取链接中表的信息
    :param url_content: 将获取的表中内容存在url_content中
    :param response: url.text内容
    :return: None
    '''
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find_all('tr')

    for row in table:
        contents = ['四川农业大学','2019']#获得表里的内容
        for element in row:
            if element.find('span') and element.find('span')!=-1:
                contents.append(element.find('span').string)

        if len(contents)>2:
            if contents[2] == '浙江':
                contents[4] = 'all'  # Category：综合改革改为all
            else:
                contents[4] = '理科'  # Category：理工改为理科
            url_content.append(contents)
    return url_content


def save_2019_contents(url_content):#将2019非链接内容写入csv
    try:
        with open("61518314周圣阳-四川农业大学.csv", 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['College','Year','Province','Category','Major','Score','Contributor'])
            for i in range(len(url_content)+1):
                writer.writerow(['四川农业大学','2019',url_content[i][0], url_content[i][1], 'all',url_content[i][3],'61518314周圣阳'])
    except:
        pass


def save_contents_2019(urlist):  # 将2019有链接内容写入csv中
    try:
        with open("61518314周圣阳-四川农业大学.csv", 'a+') as f:
            writer = csv.writer(f, lineterminator='\n')
            for i in range(1, len(urlist)):
                writer.writerow(
                    [urlist[i][0], urlist[i][1], urlist[i][2], urlist[i][4], urlist[i][3], urlist[i][6], '61518314周圣阳'])
    except:
        pass


def main_2019(url):#2019主函数
    url_content = []
    url = url
    response = check_link(url)
    get_2019_contents(url_content, response)
    #获取表中关于本科一批次的部分
    start_pos=end_pos=0
    for i in range(len(url_content)):
        if url_content[i] and url_content[i][0]=='本科一批次':
            url_content[i]=url_content[i][1:]
            start_pos=i
    for j in range(start_pos,len(url_content)):
        if url_content[j] and url_content[j][0]=='职教本科批次':
            end_pos=j
    url_content=url_content[start_pos:end_pos]
    #获取2019表中的非链接信息
    temp_content=[]
    temp_content.append(url_content[0])
    temp_content.append(url_content[1])
    #西藏的分数数据在html中格式有些问题，无法被提取出来，这里手动加入
    for i in url_content:
        if i[0]=='西藏':
            i.append('487')
            temp_content.append(i)
            break
    url_content=temp_content
    save_2019_contents(url_content)#写入非链接信息
    url_content=[]
    get_links(url_content,response)#获取表中链接
    for link in url_content:
        link_content=[]
        link_response = check_link(link)
        get_contents_2019(link_content,link_response)
        save_contents_2019(link_content)#写入链接信息


# 2018

def get_contents(url_content, response):
    '''
    获取2018、2017年的数据
    :param url_content: 将获取的表中内容存在url_content中
    :param response: url.text内容
    :return: None
    '''
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find_all('tr')

    for row in table:
        contents = []
        for element in row:
            if element:
                content = element.string
                if content:
                    content = content.replace('\n', '')#清除不必要的格式
                    content = content.replace('\r', '')
                    content = content.replace('\t', '')
                if content:
                    contents.append(content)
        url_content.append(contents)


def save_2018_contents(urlist):#将2018年数据写入csv
    try:
        with open("61518314周圣阳-四川农业大学.csv", 'a+') as f:
            writer = csv.writer(f, lineterminator='\n')
            for i in range(len(urlist)):
                writer.writerow(['四川农业大学', '2018', urlist[i][0], urlist[i][1], 'all', urlist[i][3][:3], '61518314周圣阳'])
    except:
        pass


def main_2018(url):#2018主函数
    url_content = []
    url = url
    response = check_link(url)
    get_contents(url_content, response)
    #获取本科一批次的数据
    start_pos = end_pos = 0
    for i in range(len(url_content)):
        if url_content[i] and url_content[i][0] == '本科一批次':
            url_content[i] = url_content[i][1:]
            start_pos = i
    for j in range(start_pos, len(url_content)):
        if url_content[j] and url_content[j][0] == '职教本科批次':
            end_pos = j
    url_content = url_content[start_pos:end_pos]
    #由于表格格式原因，对两个加入他们缺失的省份
    url_content[1].insert(0, '四川')
    url_content[3].insert(0, '重庆')
    save_2018_contents(url_content)#写入数据


#2017

def save_2017_contents(urlist):#将2017年数据写入csv
    try:
        with open("61518314周圣阳-四川农业大学.csv", 'a+') as f:
            writer = csv.writer(f, lineterminator='\n')
            for i in range(0, len(urlist)):
                writer.writerow(['四川农业大学', '2017', urlist[i][0], urlist[i][1], 'all', urlist[i][3][:3], '61518314周圣阳'])
    except:
        pass


def main_2017(url):#2017主函数
    url_content = []
    url = url
    response = check_link(url)
    get_contents(url_content, response)
    #获取本科一批次数据
    start_pos = end_pos = 0
    for i in range(len(url_content)):
        if url_content[i] and url_content[i][0] == '本科一批次':
            url_content[i] = url_content[i][1:]
            start_pos = i
    for j in range(start_pos, len(url_content)):
        if url_content[j] and url_content[j][0] == '职教本科批次':
            end_pos = j
    url_content = url_content[start_pos:end_pos]
    save_2017_contents(url_content)#写入数据


#执行代码
main_2019(url_2019)
main_2018(url_2018)
main_2017(url_2017)
