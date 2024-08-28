from django.db import models


# Create your models here.
class UserInfo(models.Model):
    '''用户表  '''
    name = models.CharField(verbose_name="姓名", max_length=255)  # 用户名
    password = models.CharField(verbose_name="密码", max_length=255)  # 密码
    role_choices = (
        (0, "普通用户"),
        (1, "管理员")
    )
    role = models.IntegerField(verbose_name="权限", choices=role_choices)  # 权限
    email = models.CharField(verbose_name="邮箱", max_length=255)  # 邮箱


class ProbInfo(models.Model):
    """问题实例表"""
    prob_name = models.CharField(max_length=255)  # 问题名称
    description = models.CharField(max_length=255)  # 问题描述
    dimensions = models.IntegerField()  # 问题规模
    objectives = models.IntegerField()  # 约束个数
    value_vector = models.JSONField()  # 价值矩阵
    weight_matrix = models.JSONField()  # 权重矩阵


class AlgInfo(models.Model):
    """算法信息"""
    alg_name = models.CharField(max_length=255)  # 算法名
    description = models.CharField(max_length=255)  # 算法描述


class PramInfo(models.Model):
    ''''参数信息表'''
    parm_name = models.CharField(max_length=255)  # 参数名
    type = models.CharField(max_length=255)  # 参数类型
    description = models.CharField(max_length=255)  # 参数描述
    value = models.FloatField()  # 参数值
    algorithm = models.ForeignKey(to="AlgInfo", to_field='id', on_delete=models.CASCADE, blank=True, null=True,
                                  default=None)


#
#
class Plan(models.Model):
    ''''执行计划'''
    name = models.CharField(max_length=255)  # 方案名称
    algorithms = models.TextField(blank=True, null=True)
    problems = models.TextField(blank=True, null=True)
    execution_count = models.IntegerField()  # 执行次数
    start_time = models.FloatField(default=0)  # 执行时间


class AlgResult(models.Model):
    ''''算法执行结果'''
    algorithm_name = models.CharField(max_length=255)  # 算法名
    problem_name = models.CharField(max_length=255)  # 问题名                   # 运行编号
    start_time = models.DateTimeField()  # 开始时间
    end_time = models.DateTimeField(default=None, null=True)  # 结束时间


"""迭代结果"""
class GenResult(models.Model):
    algorithm_name = models.CharField(max_length=255)  # 算法名
    coding = models.JSONField()  # 编码 (Array)
    gen_num = models.IntegerField()  # 迭代次数
    obj_value = models.FloatField()  # 目标值
    problem_instance_name = models.CharField(max_length=255)  # 问题实例名
    run = models.ForeignKey(AlgResult, to_field='id', on_delete=models.CASCADE, default=None, null=True)  # 运行编号
    end_time = models.DateTimeField()  # 结束时间
