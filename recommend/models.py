from django.db import models


# 志愿类
class CollegeApplication(models.Model):
    # 年份，整型，默认为2020年
    year_int = models.IntegerField()
    # 学校名字，字符
    school_text = models.CharField(max_length=20)
    # 专业名字，字符
    major_text = models.CharField(max_length=20)
    # 最低分数，整型，不超过999
    score_int = models.IntegerField()
    # 排名，整型
    range_int = models.IntegerField()
    # 理科or文科，布尔类型，理科sci为1，文科lib为0
    sci_or_lib = models.BooleanField()
    # 提前批or普通一批，布尔类型，adv提前批为1，普通一批com为0
    adv_or_com = models.BooleanField()
    # 专业详情
    major_situation_text = models.CharField(max_length=200,default='')

    # 定义了一个函数，查询时会返回学校名字+专业
    def __str__(self):
        return self.school_text + self.major_text