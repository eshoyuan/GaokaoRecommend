import csv
import numpy as np
from recommend.models import CollegeInformation

# 计算院校位次的平均值、方差并写入数据库
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
file_path = 'crawler/2020shandong.csv'  # 此处为需要写入的csv文件地址
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    schools = {row[0] for row in reader if reader.line_num != 1}
    for school in schools:
        with open(file_path, 'r', encoding='UTF-8') as f2:
            reader2 = csv.reader(f2)
            ranks = [float(row[5]) for row in reader2 if row[0] == school]
            print(ranks)
            mean = np.mean(ranks)
            var = np.var(ranks)
            print(mean, var)
            CollegeInformation.objects.update_or_create(school_text=school,
                                                        rank_ave_float=mean,
                                                        rank_var_float=var,
                                                        )
