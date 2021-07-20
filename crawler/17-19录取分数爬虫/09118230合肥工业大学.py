import requests
import json
import pandas as pd


def GetScore():

    # Reqeuest URL
    url = 'http://bkzs.hfut.edu.cn/f/ajax_lnfs?ts=1589509360776'

    province_list = [
        "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽",
        "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州",
        "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆", "台湾", "香港", "澳门"
    ]
    year_list = ['2017', '2018', '2019']
    catagory_list = ['文史', '理工', '综合改革']
    campus_list = ['合肥校区', '宣城校区']

    for i in range(len(year_list)):
        score_df = pd.DataFrame()  # score_df to record score
        for j in range(len(province_list)):
            for k in range(len(catagory_list)):
                for l in range(len(campus_list)):

                    # Form Data
                    formdata = {
                        'ssmc': province_list[j],
                        'zsnf': year_list[i],
                        'klmc': catagory_list[k],
                        'campus': campus_list[l],
                        'zslx': '统招一批'
                    }
                    response = requests.post(url, data=formdata)

                    if response.status_code == 200:
                        # filter
                        score = json.loads(response.text)[
                            'data']['sszygradeList']
                        if len(score) != 0:
                            for x in score:
                                score_df = score_df.append(
                                    [{
                                        'College': '合肥工业大学',
                                        'Year': x['nf'],
                                        'Province': x['ssmc'],
                                        'Category': x['klmc'],
                                        'Campus': x['campus'],
                                        'Major': x['zymc'],
                                        'Score': x['minScore'],
                                        'Contributor': '09118320鲁瀚洋'
                                    }], ignore_index=True)
                        else:
                            pass
        # save to csv
        path = '合肥工业大学' + year_list[i] + '.csv'
        score_df.to_csv(path, encoding='utf-8-sig')


if __name__ == "__main__":
    GetScore()
