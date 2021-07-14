import requests
#from bs4 import BeautifulSoup
import pandas as pd
import xlwt

Province=['83650','83671','83692','83887','84029',
          '84152','84281','84359','84515','84537',
          '84670','84783','84923','85027','85149',
          '85323','85516','85645','85795','85958',
          '86096','86125','86169','86390','86491',
          '86645','86727','86855','86968','87021',
          '87053','87172','464850','464851','470451']
#网站上各个省份的编码 
ProvinceData=['北京市','天津市','河北省','山西省','内蒙古自治区',
             '辽宁省','吉林省','黑龙江省','上海市','江苏省',
             '浙江省','安徽省','福建省','江西省','山东省',
             '河南省','湖北省','湖南省','广东省','广西壮族自治区',
             '海南省','重庆市','四川省','贵州省','云南省',
             '西藏自治区','陕西省','甘肃省','青海省','宁夏回族自治区',
             '新疆维吾尔自治区','港澳台联招','台湾免试','澳门保送','香港免试']

Subject=["文科","理科","文/理","综合改革"]

Year=["2019","2018","2017"]

temp=[]

def request_to_url(url, data):
    response = requests.post(url, data=data)
    return response.text
       
def MadeList(Subject,Year,Province,ProvinceData):
    data = { "kl":Subject,'nf': Year, 'areaId':Province} 
    html = request_to_url('http://zs.cufe.edu.cn/openinfo/scores', data)
    df = pd.read_html(html)  # 使用pandas的read_html函数对表格进行解析 
    table = df[0]
    for i in range(table.shape[0]): 
        Major = table['专业（类）'][i]  # 专业 
        Score = table['最低分'][i]  # 最低分
        if Score=='没有数据！':#过程中会出现很多这样的情况
            continue
        else:
            temp.append(['中央财经大学'])
            temp.append([Year])
            temp.append([ProvinceData])
            temp.append([Subject])
            temp.append([Major])
            temp.append([Score])
            temp.append(['09118125盛憬昊'])

for i in range(0,len(Subject)):
    for j in range(0,len(Year)):
        for k in range(0,len(Province)):
            MadeList(Subject[i],Year[j],Province[k],ProvinceData[k])
print(temp)

book = xlwt.Workbook()     #创建工作簿        
sheet = book.add_sheet('Sheet1')           #创建工作表格
sheet.write(0,0,'College') 
sheet.write(0,1,'Year')  
sheet.write(0,2,'Province') 
sheet.write(0,3,'Category') 
sheet.write(0,4,'Major') 
sheet.write(0,5,'Score') 
sheet.write(0,6,'Contibutor')  
for i in range(0,len(temp)//7):
    sheet.write(i+1,0,str(temp[i*7]))
    sheet.write(i+1,1,str(temp[i*7+1]))
    sheet.write(i+1,2,str(temp[i*7+2]))
    sheet.write(i+1,3,str(temp[i*7+3]))
    sheet.write(i+1,4,str(temp[i*7+4]))
    sheet.write(i+1,5,str(temp[i*7+5]))
    sheet.write(i+1,6,str(temp[i*7+6]))
    
book.save(r'C:\Users\18220\Desktop\新建文件夹\09118125盛憬昊_中央财经大学.xls')   


