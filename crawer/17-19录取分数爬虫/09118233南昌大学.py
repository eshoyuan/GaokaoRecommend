import requests                                         
from bs4 import BeautifulSoup                            
import bs4
import re
import csv

##################获取不同年份的链接#########################################
def get_year(url,header): 
    link_list=['http://zjc.ncu.edu.cn/zszx/lnfs/']*5           #用于保存链接
    r=requests.get(url,headers=header)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    data=r.text
    soup=BeautifulSoup(data,"html.parser")
    index=0
    for t in soup.find_all('ul'):                              #找寻所有标签为ul的元素
        if t.get('class')==['am-list']:                        #找到表格
            for i in soup.find_all('a'):                       #找寻所有标签为a的元素
                ########筛选所需要的链接##########
                pattern=re.compile("一批次")                    
                s=pattern.findall(str(i.string))
                pattern1=re.compile("本科批次")
                s1=pattern1.findall(str(i.string))
                if i.get('class')==['am-list-item-hd'] and (len(s)!=0 or len(s1)!=0):
                    link_list[index]+=i.get('href')           #把符合条件的链接存入list
                    index+=1
    return link_list
      
##################获取当前链接下的分数线信息################################
def get_data(url,n,header):
    fraction_list=[]                                                                               
    try:
        r=requests.get(url,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        data=r.text
        soup=BeautifulSoup(data,"html.parser")
        for tr in soup.find('tbody').children:              #找寻标签为tbody的元素的子集
            if isinstance(tr,bs4.element.Tag):
                tds=tr('td')
                ############根据不同的年份调整信息的顺序和格式#####################
                if (n==2019):
                    fraction_list.append(["南昌大学",n,tds[1].string.strip(),tds[2].string.strip(),tds[0].string.strip(),tds[5].string.strip(),"孔译轮"])
                elif (n==2018):
                    fraction_list.append(["南昌大学",n,tds[0].string.strip(),tds[2].string.strip(),tds[1].string.strip(),tds[4].string.strip(),"孔译轮"])
                elif (n==2017):
                    fraction_list.append(["南昌大学",n,tds[0].string.strip(),tds[1].string.strip(),tds[2].string,tds[4].string.strip(),"孔译轮"])
                else:
                    ""
        return fraction_list
            
    except:
        return ""

####################################将分数线信息存入csv文件#########################################
def save_csv(fraction_list,h=False,new=False):
    ######判断是否为首次打开csv，若是则添加表头，不是则追加信息######
    if new==True:
        output=open('E:/课程/大二下/软件实践/爬虫/data.csv','w+',newline='',encoding='utf-8-sig')
        csv_writer=csv.writer(output)
        head=['College','Year','Province','Category','Major','Score','Contributor']
        csv_writer.writerow(head)
    else:
        output=open('E:/课程/大二下/软件实践/爬虫/data.csv','a+',newline='',encoding='utf-8-sig')
        csv_writer=csv.writer(output)
        
    for i in range(len(fraction_list)):        #根据分数线信息调整输入格式
        if h==False:
            h=True
            continue
        csv_writer.writerow(fraction_list[i])
    output.close()

#######################主函数####################
def main():
    header={'User-Agent':                         #使服务器认为是浏览器在访问
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
    url = 'http://zjc.ncu.edu.cn/zszx/lnfs/index.htm'               #南昌大学历年分数线首页
    link_list=get_year(url,header)                                  #调用get_year把每年的链接存入list
    for i in range(len(link_list)):
        fraction_list=get_data(link_list[i],int(2019-i/2+0.5),header)          #调用get_data把该年的分数线存入list
        #######根据年份设置参数#########
        if i ==0:
            new=True
        else:
            new=False
        if i==2:
            h=True
        else:
            h=False
        save_csv(fraction_list,h,new)

if __name__ =="__main__":
    main()
