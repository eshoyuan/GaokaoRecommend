
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv


# In[61]:


#国防科技大学本科招生网无2019年数据
url1 = "http://gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2018/738.html"    #国防科技大学2018年录取分数统计网站
r1 = requests.get(url1)
#print(r.status_code)
#print(r.content.decode('utf-8'))

url2 = "http://gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2018/735.html"    #国防科技大学2017年录取分数统计网站
r2 = requests.get(url2)

url3 = "http://gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2017/717.html"    #国防科技大学2016年录取分数统计网站
r3 = requests.get(url3)


# In[62]:


soup1 = BeautifulSoup(r1.content.decode('utf-8'), 'html.parser')
soup2 = BeautifulSoup(r2.content.decode('utf-8'), 'html.parser')
soup3 = BeautifulSoup(r3.content.decode('utf-8'), 'html.parser')
#print(soup1)


# In[77]:


csv_file = open('61518125黄腾-国防科技大学.csv', 'w', encoding='gbk', newline='')              #建立csv文件
writer = csv.writer(csv_file)

writer.writerow(["College", "Year", "Province", "Category", "Major", "Score", "Contributor"])  # 写入标题


# In[78]:


table1 = soup1.find('tbody')                                                     #网页中分数统计在表格内，标签为'table'            
#print(table)
all_provinces1 = table1.find_all('tr')[3:33]                                     #每一行（标签'tr'）为各省份具体数据，从表格第4行开始


for each_pro in all_provinces1:
    all_td_tag = each_pro.find_all('td')                                         #每一列标签为'td'
    prov = all_td_tag[0].find('span', style = "color:rgb(0,0,0);").string        #省份
    province = prov.replace('\xa0','')                                           #'\xa0'即 &nbsp 输出为csv文件时为'?'，将其替换
    if len(all_td_tag) == 9:                                                     #原网页表格中有省份一本线与二本线相同，少一列
        score0 = all_td_tag[4].find('span', style = "font-family:宋体;").string  #非指挥类分数 #国防科技大学不分文理科，但分为非指挥类和指挥类
        score1 = all_td_tag[7].find('span', style = "font-family:宋体;").string  #指挥类分数
    else: 
        score0 = all_td_tag[3].find('span', style = "font-family:宋体;").string
        score1 = all_td_tag[6].find('span', style = "font-family:宋体;").string
    #print(len(all_td_tag))
    print('province:{}, score0:{}, score1:{}'.format(province,score0,score1))
    
    writer.writerow(["国防科技大学", "2018", province, "非指挥类", "all", score0, "61518125黄腾"])
    writer.writerow(["国防科技大学", "2018", province, "指挥类", "all", score1, "61518125黄腾"])
    
print("write_finished!")


# In[79]:


table2 = soup2.find('tbody')                                                     #网页中分数统计在表格内，标签为'table'            
#print(table)
all_provinces2 = table2.find_all('tr')[3:33]                                     #每一行（标签'tr'）为各省份具体数据，从表格第4行开始

for each_pro in all_provinces2:
    all_td_tag = each_pro.find_all('td')                                         #每一列标签为'td'
    prov = all_td_tag[0].find('span', style = "font-size: large;").string        #省份
    province = prov.replace('\xa0','')                                           #'\xa0'即 &nbsp 输出为csv文件时为'?'，将其替换
    if len(all_td_tag) == 9:                                                     #原网页表格中有省份一本线与二本线相同，少一列
        score0 = all_td_tag[4].find('span', style = "font-family: 宋体;").string  #非指挥类分数 #国防科技大学不分文理科，但分为非指挥类和指挥类
        score1 = all_td_tag[7].find('span', style = "font-family: 宋体;").string  #指挥类分数
    else: 
        score0 = all_td_tag[3].find('span', style = "font-family: 宋体;").string
        score1 = all_td_tag[6].find('span', style = "font-family: 宋体;").string
    #print(len(all_td_tag))
    print('province:{}, score0:{}, score1:{}'.format(province,score0,score1))
    
    writer.writerow(["国防科技大学", "2017", province, "非指挥类", "all", score0, "61518125黄腾"])
    writer.writerow(["国防科技大学", "2017", province, "指挥类", "all", score1, "61518125黄腾"])
     
print("write_finished!")


# In[80]:


table3 = soup3.find('tbody')                                                     #网页中分数统计在表格内，标签为'table'            
#print(table)
all_provinces3 = table3.find_all('tr')[3:33]                                     #每一行（标签'tr'）为各省份具体数据，从表格第4行开始

for each_pro in all_provinces3:
    all_td_tag = each_pro.find_all('td')                                         #每一列标签为'td'
    prov = all_td_tag[0].find('span', style = "font-size: 14pt;").string         #省份
    province = prov.replace('\xa0','')                                           #'\xa0'即 &nbsp 输出为csv文件时为'?'，将其替换
                                                                                 #2016年表格中无省份一本线与二本线相同，均为8列
    score0 = all_td_tag[3].find('span', style = "font-family: 华文中宋;").string #工程技术类分数 #2016年不分文理科，但分为非工程技术类和学历教育合训类
    score1 = all_td_tag[6].find('span', style = "font-family: 华文中宋;").string #学历教育合训类分数

    #print(len(all_td_tag))
    print('province:{}, score0:{}, score1:{}'.format(province,score0,score1))
    
    writer.writerow(["国防科技大学", "2016", province, "工程技术类", "all", score0, "61518125黄腾"])
    writer.writerow(["国防科技大学", "2016", province, "学历教育合训类", "all", score1, "61518125黄腾"])

csv_file.close()
print("write_finished!")


# In[ ]:




