from django.db import models

# Create your models here.
'''算法信息表'''
class AlgInfo(models.Model):
    alg_name = models.CharField(max_length=255)  #算法名
    description = models.TextField()              #算法描述

''''参数信息表'''
class PramInfo(models.Model):
    parm_name = models.CharField(max_length=255)     #参数名
    type=models.CharField(max_length=255)            # 参数类型
    description = models.TextField()                 #  参数描述
    value=models.FloatField()                        # 参数值
    algorithm = models.ForeignKey(AlgInfo,to_field='id', on_delete=models.CASCADE, default=None, null=True)


