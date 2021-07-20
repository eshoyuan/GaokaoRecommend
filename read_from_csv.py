import csv
from recommend.models import CollegeApplication
# 读取2020年院校专业的志愿信息
# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
file_path = 'crawler/new16-20.csv'  # 此处为需要写入的csv文件地址
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # 跳过第一行
        if reader.line_num == 1 and row[3] != 2020:
            continue
        print(row[6])
        CollegeApplication.objects.update_or_create(school_text=row[0],
                                                    major_text=row[1],
                                                    score_int=row[4],
                                                    range_int=row[5],
                                                    major_situation_text=row[2],
                                                    is_985=row[8],
                                                    is_211=row[9],
                                                    id=reader.line_num-1)
