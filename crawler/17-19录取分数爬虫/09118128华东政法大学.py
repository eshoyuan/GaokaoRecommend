import selenium.webdriver as webdriver
import selenium.webdriver.support.select as select
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time


def save_csv(data):
    data = pd.DataFrame(data, columns=["Year","Province","Category","Major","Score"]) 
    data.insert(0,'College',"华东政法大学")
    data["Contributor"]="09118128李英泰"
    data.to_csv("09118229李英泰-华东政法大学.csv",encoding='ascii',index=False)
#需要循环的部分
#跳转窗口后重新定位
def get_infomation():
    for i in range(5,9):
        for j in range(0,30):
            browser.switch_to_window(browser.window_handles[1])
            time.sleep(1)
            year=browser.find_element_by_xpath('//*[@id="frm1:year"]')
            select_year=select.Select(year)
            select_year.select_by_index(i)#6,7,8
            time.sleep(1)
            province=browser.find_element_by_xpath('//*[@id="frm1:province"]')
            select_province=select.Select(province)
            select_province.select_by_index(j)#0~30
            page=BeautifulSoup(browser.page_source,'html.parser')
            ''''''
            info_unprocessed=[]
            trs=page.find_all('tr')
            for tr in trs:
                info=[]
                for td in tr:
                    if td.string==None:
                        if 'dt_c_w140_c' in td.attrs:
                            info.append(td['dt_c_w140_c'])
                    else:
                        info.append(td.string)
                info_unprocessed.append(info)#从page.text抽取信息
            for info in info_unprocessed:
                if len(info)==14:
                    data.append([2011+i,province_list[j],info[3],info[5],info[9]])
data=[]
year=['2012','2011','2013','2014','2015','2016','2017','2018','2019','2020']
province_list=['北京市','天津市','重庆市','上海市','内蒙古自治区','辽宁省',
'吉林省','江苏省','山西省','黑龙江省','浙江省','安徽省','福建省','江西省',
'新疆维吾尔自治区','河南省','湖北省','湖南省','广东省','广西壮族自治区',
'海南省','河北省','四川省','贵州省','西藏自治区','云南省','陕西省','甘肃省',
'青海省','宁夏回族自治区','山东省']

url='https://zsb.ecupl.edu.cn/'
browser=webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('//*[@id="Map"]/area[1]').click()
get_infomation()
browser.quit()
save_csv(data)




