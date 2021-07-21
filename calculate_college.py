import csv
import numpy as np
from recommend.models import CollegeInformation
# 计算院校位次的平均值、方差并写入数据库
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
file_path = 'crawler/2020shandong.csv'  # 此处为需要写入的csv文件地址
schools = []
ranks = []
e = []
readerlist=[]
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # 跳过第一行和年份不为2020年的部分
        if reader.line_num == 1:
            continue
        schools.append(row[0])
    e = list(set(schools))
    e.sort(key=schools.index)
    # print(e)
    # f.close()
    with open(file_path, 'r', encoding='UTF-8') as ff:
        reader = csv.reader(ff)
        readerlist = list(reader)
        readerlist = readerlist[1:]
    for school in e:
        for r in readerlist:
            if school == r[0]:
                ranks.append(float(r[5]))
        mean = np.mean(ranks)
        var = np.var(ranks)
        #print(school, mean, var)
        ranks.clear()
        CollegeInformation.objects.update_or_create(school_text=school,
                                                    rank_ave_float=mean,
                                                    rank_var_float=var
                                                    )

