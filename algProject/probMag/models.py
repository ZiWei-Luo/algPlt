from django.db import models

"""问题实例表"""
class ProbInfo(models.Model):
    prob_name = models.CharField(max_length=255)  #问题名称
    description = models.TextField()     #问题描述
    dimensions = models.IntegerField()    #问题规模
    objectives = models.IntegerField()     #约束个数
    value_vector = models.JSONField()  # 价值矩阵
    weight_matrix = models.JSONField()    # 权重矩阵