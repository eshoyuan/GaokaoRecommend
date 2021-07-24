from django.db import models


# 2020年志愿的详情，作为推荐的主要因素
class CollegeApplication(models.Model):
    # 学校名字，字符
    school_text = models.CharField(max_length=20, default='')
    # 专业名字，字符
    major_text = models.CharField(max_length=20, default='')
    # 最低分数，整型，不超过999
    score_int = models.IntegerField(default=0)
    # 排名，整型
    rank_int = models.IntegerField(default=0)
    # 专业详情
    major_situation_text = models.CharField(max_length=200, default='')
    # 985
    is_985 = models.BooleanField(default=0)
    # 211
    is_211 = models.BooleanField(default=0)
    # 专业选课要求,0表示不作要求，1表示选一个即可，-1表示都要选
    Phy = models.IntegerField(default=0)
    Che = models.IntegerField(default=0)
    Bio = models.IntegerField(default=0)
    Pol = models.IntegerField(default=0)
    His = models.IntegerField(default=0)
    Geo = models.IntegerField(default=0)
    # 0表示符合一门即可，1表示都要符合
    request = models.IntegerField(default=0)

    # 定义了一个函数，查询时会返回学校名字+专业
    def __str__(self):
        return self.school_text + self.major_text

    # 定义数据表
    class Meta:
        db_table = 'recommend_application'


# 用作2020年某个院校所有专业的平均位次，方差等数据，也作为院校选择的一部分因素，权衡学校内部专业水平
class CollegeInformation(models.Model):
    school_text = models.CharField(max_length=20)
    # 排名平均值，浮点数
    rank_ave_float = models.FloatField(default=0)
    # 排名方差，浮点数
    rank_var_float = models.FloatField(default=0)


# 用作展示某个院校某个专业的位次变化，用作图表表示趋势
class MajorRank(models.Model):
    # 学校名字，字符
    objects = None
    school_text = models.CharField(max_length=40)
    # 专业名字，字符
   #major_text = models.CharField(max_length=20)
    # 2016排名，整型
    rank_2016 = models.IntegerField(default=0)
    # 2017排名，整型
    rank_2017 = models.IntegerField(default=0)
    # 2018排名，整型
    rank_2018 = models.IntegerField(default=0)
    # 2019排名，整型
    rank_2019 = models.IntegerField(default=0)
    # 2020排名，整型
    #rank_2020 = models.IntegerField(default=0)
    class Meta:
        db_table = 'recommend_majorrank'
#预测录取名次
class Collegeprediction(models.Model):
    school_text = models.CharField(max_length=40)
    pre_rank=models.IntegerField(default=-1)
    pre_acc=models.CharField(max_length=200)
    class Meta:
        db_table = 'recommend_prediction'

