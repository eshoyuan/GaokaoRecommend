import csv
from recommend.models import Collegelast
# 读取2020年院校专业的志愿信息
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
# 物化生政史地，提取选课要求
# 0表示不作要求，1表示有要求；对于'要求'，0表示多选一，1表示多选多
def parser(subject):
    subject_request = {'物': 0, '化': 0, '生': 0, '政': 0, '史': 0, '地': 0, '要求': 0}
    requirement1 = subject.split('/')
    requirement2 = subject.split('、')
    if subject != '不限':
        if len(requirement1) >= len(requirement2):
            for i in requirement1:
                subject_request[i] = 1
        else:
            for i in requirement2:
                subject_request[i] = 1
            subject_request['要求'] = 1
    return subject_request

file_path = 'crawler/16-20shandong.csv'  # 此处为需要写入的csv文件地址

with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # 跳过第一行和年份不为2020年的部分
        if reader.line_num == 1 and row[3] != 2020:
            continue
        subject_request = parser(row[6])
        Collegelast.objects.update_or_create(school_text=row[0],
                                             major_text=row[1],
                                             major_situation_text=row[2],
                                             rank_int=row[5],
                                             year_int=row[3]
                                             )
