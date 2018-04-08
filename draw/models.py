from django.db import models

# Create your models here.

class Test(models.Model):
    # 索引
    index = models.IntegerField()
    # 站点编号
    station = models.IntegerField()
    # 频率
    fre = models.DecimalField(max_digits=14, decimal_places=2)
    # 出现时间
    app_time = models.DateTimeField()
    # 消失时间
    disapp_time = models.DateTimeField()
    #　背景电平
    back_level = models.DecimalField(max_digits=5, decimal_places=2)
    # 电平
    level = models.DecimalField(max_digits=5, decimal_places=2)
    # 出现标志
    flag = models.IntegerField()

    class Meta(object):
        db_table = 'test'
