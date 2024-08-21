from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=255)       #用户名
    password = models.CharField(max_length=255)   #密码
    role = models.IntegerField(default=0)          #权限
    email = models.CharField(max_length=255)       #邮箱