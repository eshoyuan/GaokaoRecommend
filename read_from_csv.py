import csv
from recommend.models import CollegeApplication

# 输入 python manage.py shell， 复制整个代码粘贴后运行即可
file_path = 'SEU_RecommenderSystem/syy_crawer/16-20.csv'  # 此处为需要写入的csv文件地址
with open(file_path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # 跳过第一行
        if reader.line_num == 1:
            continue
        print(row[6])
        if row[6] == '理科':
            A = 1
        elif row[6] == '文科':
            A = 0
        if row[7] == '本科提前批':
            B = 1
        elif row[7] == '本科批' or row[7] == '本科一批':
            B = 0
        # 年份自己手动修改
        CollegeApplication.objects.update_or_create(year_int=row[3],
                                                    school_text=row[0],
                                                    major_text=row[1],
                                                    score_int=row[4],
                                                    range_int=row[5],
                                                    sci_or_lib=A,
                                                    adv_or_com=B,
                                                    major_situation_text=row[2])
