from django.db import models

"""算法结果"""
class AlgResult(models.Model):
    algorithm_name = models.CharField(max_length=255)  # 算法名
    problem_name = models.CharField(max_length=255)    # 问题名
    run_id = models.IntegerField()                     # 运行编号
    start_time = models.DateTimeField()                 # 开始时间
    end_time = models.DateTimeField()                   # 结束时间

"""迭代结果"""
class GenResult(models.Model):
    algorithm_name = models.CharField(max_length=255)  # 算法名
    coding = models.JSONField()                         # 编码 (Array)
    gen_num = models.IntegerField()                  # 迭代次数
    obj_value = models.FloatField()               # 目标值
    problem_instance_name = models.CharField(max_length=255)  # 问题实例名
    run_id = models.IntegerField()                     # 运行编号
    end_time = models.DateTimeField()                   # 结束时间

