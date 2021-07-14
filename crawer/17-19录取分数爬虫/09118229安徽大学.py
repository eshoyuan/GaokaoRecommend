import pandas as pd

def get_data(url):
    data_all=pd.read_html(url)[6]                                        #得到原始数据
    data_1=data_all.iloc[[8,12,19],2:28]                                 
    data_2=data_all.iloc[30:36,[0,4,5,9]]
    year=data_all[0][0][4:8]                                             #判断当前页面是哪一年的录取分数线
    data=[]
    for i in data_1.columns:                                             #除上海、浙江外的录取分数线（无专业分数）
        data.append([year,data_1[i][8],"文科","all",data_1[i][12]])
        data.append([year,data_1[i][8],"理科","all",data_1[i][19]])
    data.append([year,"上海","文科","all",data_all[1][26]])              #上海高考改革单独招生（无专业分数）
    data.append([year,"上海","理科","all",data_all[3][26]])     
    for i in data_2.index:                                               #浙江高考改革单独招生（有专业分数）
        data.append([year,"浙江","all",data_2[0][i],data_2[4][i]])
        data.append([year,"浙江","all",data_2[5][i],data_2[9][i]])  
    return data                                                          #返回的是列表

def save_csv(data):
    data_df = pd.DataFrame(data, columns=["Year","Province","Category","Major","Score"]) 
    data_df.insert(0,'College',"安徽大学")
    data_df["Contributor"]="09118229张博宇"
    data_df.to_csv("09118229张博宇-安徽大学.csv",encoding='utf-8',index=False)
    
def main():
    url=['http://zsb.ahu.edu.cn/2019/1017/c13340a210925/page.htm',       #2019年的数据源url
         'http://zsb.ahu.edu.cn/2018/1015/c13340a187840/page.htm',       #2018年的数据源url
         'http://zsb.ahu.edu.cn/2018/0418/c13340a164446/page.htm']       #2017年的数据源url
    data=[]
    for i in url:
        data+=get_data(i)        
    save_csv(data)

if __name__ == '__main__':
    main()  
    
