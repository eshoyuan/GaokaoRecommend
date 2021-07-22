import csv
import numpy as np
from recommend.models import MajorRank
# 按照某个院校某个专业的位次变化读取，用作图表表示趋势
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
schools = {}
file_path = 'crawler/16-19shandong.csv'  # 此处为需要写入的csv文件地址
schools = []
e = []
readerlist = []
r16 = 0
r17 = 0
r18 = 0
r19 = 0
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # 跳过第一行和年份不为2020年的部分
        if reader.line_num == 1:
            continue
        schools.append(row[0] + row[1])
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
            if (school.strip() == (r[0] + r[1]).strip()) and r[3] == '2016':
                r16 = r[5]
            if (school.strip() == (r[0] + r[1]).strip()) and r[3] == '2017':
                r17 = r[5]
            if (school.strip() == (r[0] + r[1]).strip()) and r[3] == '2018':
                r18 = r[5]
            if (school.strip() == (r[0] + r[1]).strip()) and r[3] == '2019':
                r19 = r[5]
        MajorRank.objects.update_or_create(school_text=school,
                                           rank_2016=r16,
                                           rank_2017=r17,
                                           rank_2018=r18,
                                           rank_2019=r19)
