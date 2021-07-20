import pandas as pd

#根据观察，不同省份的url间只有两位数有差异，将两位数和省份相互对应，用字典形式储存
province_list=[
        "山西","河北","天津","北京","内蒙古","浙江","江苏","上海","黑龙江","吉林","辽宁","湖北","河南",
        "山东","江西","福建","安徽","四川","重庆","海南","广西","广东","湖南","贵州","新疆","宁夏","青海",
        "甘肃","陕西","云南"]
num_list=range(40,70)
province_dict=dict(zip(num_list,province_list))


#定义爬虫，输入为url和与省份对应的数，返回为某省包含三年数据的列表。
def crawl(num,url):
    data=pd.read_html(url)[0]
    data_year=data.iloc[14:,0]#爬取年份
    data_score=data.iloc[14:,4]#爬取最低分
    data_select=[]
    for i in range(3):
        data_select.append(["中国科学技术大学",data_year.iloc[i],province_dict[num],
                            "all","all",data_score.iloc[i],"09118228沈飞鸿"])#其他数据都未显示，故自定义
    return data_select
    
   

#主函数
if __name__=='__main__':
    result=[]
    #通过一个循环来获取不同省份的数据
    for num in num_list:
        url="https://zsb.ustc.edu.cn/2017/0405/c12994a1815" + str(num) + "/page.htm"
        result+=crawl(num,url)
    
    #将数据用DateFrame储存，并加上表头。    
    result_df=pd.DataFrame(result,columns=["College","Year","Province","Category",
                                          "Major","Score","Contributor"])
    #保存到csv文件
    result_df.to_csv(r'09118228沈飞鸿-中国科学技术大学.csv',mode='a',encoding='utf_8_sig',header=1,index=0)
    