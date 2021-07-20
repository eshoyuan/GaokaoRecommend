import requests
import json
import pandas as pd

def bjtupost(sort=None, year=None, province=None):
    url = 'https://zsw.bjtu.edu.cn/score/query.html'
    From_data = {'sort': sort, 'type': '非定向', 'school': '校本部',
                 'year': year, 'province': province}
    Headers = {'X-Requested-With': 'XMLHttpRequest'}
    response = requests.post(url, data=From_data, headers=Headers)
    content = json.loads(response.text)
    return content['data'][3:]


provinces = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林',
             '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西',
             '山东', '河南', '湖北', '湖南', '广东', '广西', '河南',
             '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃',
             '青海', '宁夏', '新疆', '港澳台侨']
years = ['2019', '2018', '2017']
sorts = ['理工', '文史']

College = []
Year = []
Province = []
Category = []
Major = []
Score = []
Contributor = []

if __name__ == '__main__':
    for year in years:
        for province in provinces:
            for sort in sorts:
                result = bjtupost(sort, year, province)
                for i in range(len(result)):
                    College.append('北京交通大学')
                    Year.append(year)
                    Province.append(province)
                    Category.append(result[i]['xkml'])
                    Major.append(result[i]['zymc'])
                    Score.append(result[i]['zdf'])
                    Contributor.append('09118104谈笑')

all_data = {'College': College, 'Year': Year, 'Province': Province, 'Category': Category,
            'Major': Major, 'Score': Score, 'Contributor': Contributor}

all_data_df = pd.DataFrame(all_data)
all_data_df.to_csv('09118104谈笑-北京交通大学.csv', index=False)



