from django.db import models


# 志愿类
class CollegeApplication(models.Model):
    # 学校名字，字符
    school_text = models.CharField(max_length=20)
    # 专业名字，字符
    major_text = models.CharField(max_length=20)
    # 最低分数，整型，不超过999
    score_int = models.IntegerField(max_length=3)
    # 排名，整型
    range_int = models.IntegerField(max_length=10)
    # 理科or文科，布尔类型，理科sci为1，文科lib为0
    sci_or_lib = models.BooleanField()
    # 提前批or普通一批，布尔类型，adv提前批为1，普通一批com为0
    adv_or_com = models.BooleanField()
