import csv
import numpy as np
from recommend.models import MajorRank

# 按照某个院校某个专业的位次变化读取，用作图表表示趋势
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
file_path = 'crawer/new16-20.csv'  # 此处为需要写入的csv文件地址
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    schools = {row[0] for row in reader if reader.line_num != 1}
    for school in schools:
        MajorRank.objects.update_or_create(school_text=school,
                                           major_text=_text=school,
                                            rank_2016=mean,
                                            rank_2017=var,
                                            rank_2018=var,
                                            rank_2019=var,
                                            rank_2020=var,)
