import pandas as pd

'''
贵州大学分数线数据爬取
2019年为所有省市分数线
2018年分为省内和省外分数线
2017年官网没有数据
一共三个网页
'''


# 爬取数据
def craw(url, name):
    tb = pd.read_html(url)[0]
    tb.to_csv(name,  mode='a', encoding='utf-8', header=0, index=0)


# 增加学校年度以及提供人
def insertion(file, year):
    file.insert(0, 'Year', year)
    file.insert(0, 'College', '贵州大学')
    file['Contributor'] = '61518319司翀杰'


url1 = 'http://rso.gzu.edu.cn/web/article/7883'
url2 = 'http://rso.gzu.edu.cn/web/article/7796'
url3 = 'http://rso.gzu.edu.cn/web/article/7792'

craw(url1, '2019.csv')
craw(url2, '2018ex.csv')
craw(url3, '2018in.csv')

file2019 = pd.read_csv('2019.csv', header=None, names=['q', 'Province', 'w', 'Category', 'Major', 'Score', 'e'])
file2018ex = pd.read_csv('2018ex.csv', header=None, names=['Province', 'Category', 'Major', 'Score', 'ps'])
file2018in = pd.read_csv('2018in.csv', header=None, names=['Category', 'Major', 'Score', 'ps'])

file2019 = file2019.iloc[1:, [1, 3, 4, 5]]
insertion(file2019, 2019)
file2019.loc[1] = ['College', 'Year','Province', 'Category', 'Major', 'Score', 'Contributor']
file2019.to_csv('61518319司翀杰-贵州大学.csv', mode='a', encoding='utf-8', header=0, index=0)


file2018ex = file2018ex.iloc[1:]
file2018ex = file2018ex.drop(file2018ex[file2018ex.ps == '最高分'].index)
file2018ex = file2018ex.iloc[:, :-1]
insertion(file2018ex, 2018)
file2018ex.to_csv('61518319司翀杰-贵州大学.csv', mode='a', encoding='utf-8', header=0, index=0)

file2018in = file2018in.drop(file2018in[file2018in.ps == '最高分'].index)
file2018in = file2018in.iloc[:, :-1]
file2018in.insert(0, 'Province', '贵州省')
insertion(file2018in, 2018)
file2018in.to_csv('61518319司翀杰-贵州大学.csv', mode='a', encoding='utf-8', header=0, index=0)
