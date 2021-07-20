import csv
import numpy as np
from recommend.models import CollegeInformation

# 计算院校位次的平均值、方差并写入数据库
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
file_path = 'crawer/new16-20.csv'  # 此处为需要写入的csv文件地址
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    schools = {row[0] for row in reader if reader.line_num != 1}
    for school in schools:
        ranges = [row[5] for row in reader if row[0] == school]
        mean = np.mean(ranges)
        var = np.var(ranges)
        CollegeInformation.objects.update_or_create(school_text=school,
                                                    range_ave_float=mean,
                                                    range_var_float=var,
                                                    )
