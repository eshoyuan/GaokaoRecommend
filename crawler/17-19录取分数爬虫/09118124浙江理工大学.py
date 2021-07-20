import requests
import csv
from bs4 import BeautifulSoup

years=['2019','2018','2017']

URL1='http://zs.zstu.edu.cn/info/1007/3258.htm' #2019
URL2='http://zs.zstu.edu.cn/info/1007/3047.htm' #2018
URL3='http://zs.zstu.edu.cn/info/1007/2839.htm' #2017
URL=[URL1,URL2,URL3]

#参数为爬取年份和对应网址
def crawl(url,crawl_year):

  headers={
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
  }

  r = requests.get(url, headers=headers)

  '''
  print(type(r))
  print(r.status_code)
  print(r)
  r.encoding='utf-8'
  '''

  soup = BeautifulSoup(r.text,"lxml") #html.parser

  tables=soup.find_all('table')
  #print(len(tables))
  tab=tables[0]
  with open('09118124李翔宇-浙江理工大学.csv','a',newline='')as f:
    csv_write=csv.writer(f,dialect='excel')
        
    all_tr=tab.tbody.find_all('tr')
    del all_tr[0] #删除表头
    
    first_tr_province='' #由于2018和2017的表中，同一省份的多条tr记录里只有第一条记录有省份，所以需要第一条记录的province来填入当前记录的province
    for tr in all_tr:  #tr为一条记录
      college = '浙江理工大学'
      year=crawl_year
      province =''
      category =''
      major = 'all' #没有各专业的分数线，只有学校的录取线
      score =''
      contributor='09118124李翔宇'
      batch ='' #录取批次，判断新疆西藏的多条记录时需要使用，这里我们只取批次为汉族或内地班的文理录取线
      
      temp=tr.find_all('td') #td为一条记录里的内容
      
      #存在表中套表的情况，根据记录的长度trlen来确定所需信息的位置
      trLen=len(temp)
      
      if year == '2019':
        if trLen==9:
          province = temp[1].get_text()
          batch = temp[2].get_text()
          category = temp[3].get_text()
          score  = temp[6].get_text()
        else:  #trLen==8
          province = temp[0].get_text()
          batch = temp[1].get_text()
          category = temp[2].get_text()
          score  = temp[5].get_text()
          
      if year == '2018' or year == '2017':
        if trLen == 9:
          province = temp[1].get_text()
          first_tr_province=temp[1].get_text() #第一条记录的省份
          batch = temp[2].get_text()
          category = temp[3].get_text()
          score = temp[6].get_text()
        else:  # trLen==7
          province = first_tr_province  #第一条记录的province来填入当前记录的province
          batch = temp[0].get_text()
          category = temp[1].get_text()
          score = temp[4].get_text()


        
      #对于新疆西藏省，录取形式复杂要单独考虑
      if province=='新疆':
        if batch=='内地班' and category in ['文科','理科','汉语言理','汉语言文']:
          #满足写入条件，则统一修改为理科或文科写入
          if category=='汉语言理':
            category='理科'
          if category=='汉语言文':
            category='文科'
            
        else:#不满足写入条件
            continue #跳至下一条记录
        
      if province=='西藏':
        list=[['1汉族','理科'],
              ['1汉族','文科'],
              ['汉族','理科'],
              ['汉族','文科'],
              ['1','理科'],
              ['1','文科']]
        if [batch,category] not in list:#不满足写入条件
          continue #跳至下一条记录
      
      #对于浙江上海等综合改革省
      if category not in ['文科','理科']:
        category='all'
    
      #写入一条记录
      string=[college,year,province,category,major,score,contributor]
      csv_write.writerow(string)
    
#crawl函数end
 

#先写表头
with open('09118124李翔宇-浙江理工大学.csv','a',newline='')as f:
  csv_write=csv.writer(f,dialect='excel')
  head=['College','Year','Province','Category','Major','Score','Contributor']
  csv_write.writerow(head)

crawl(URL[0],years[0])
crawl(URL[1],years[1])
crawl(URL[2],years[2])
