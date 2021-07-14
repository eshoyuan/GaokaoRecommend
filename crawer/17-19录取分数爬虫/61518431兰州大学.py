import requests,csv,os


class lanzhou():
    def __init__(self):
        self.url = 'http://yx.lzu.edu.cn/lzuzsb/yx/scorezy/searchList'
        self.headers = {
            'Referer': 'http://yx.lzu.edu.cn/lzuzsb/stuweb/scoreweb/score.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
        self.year_list = ['2019年','2018年','2017年']
        self.parse()
    def get_html(self,url,params=None):
        res = requests.get(url,headers=self.headers,params=params)
        return res.json()
    def write_csv(self,year,province,data):
        for da in data:
            data_dict = {}
            data_dict['College'] = '兰州大学'
            data_dict['Year'] = year.split('年')[0]
            data_dict['Province'] = province
            data_dict['Category'] = da['kl']
            data_dict['Major'] = da['zy']
            data_dict['Score'] = da['zdf'].split('（')[0]
            data_dict['Contributor'] = '61518431郁航远'
            print(data_dict)
            if not os.path.exists('兰州大学.csv'):
                with open('兰州大学.csv', 'w') as f:
                    w = csv.DictWriter(f, data_dict.keys())
                    w.writeheader()
            with open('兰州大学.csv', "a", newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
                writer.writerow(data_dict)
    def parse(self):
        province_url = 'http://yx.lzu.edu.cn/lzuzsb/yx/scoresf/getCodelist?field=sf'
        province_list = self.get_html(province_url)
        for province in province_list:
            for year in self.year_list:
                params = {
                    'sf': province['NAME'],
                    'nf': year,
                    'cxkl':'',
                    'lb':''
                }
                res = self.get_html(self.url,params)
                print(res)
                self.write_csv(year,province['NAME'],res)
                # break
            # break
if __name__ == '__main__':
    lanzhou()