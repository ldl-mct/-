from django.db import models

# Create your models here.
# 创建新闻的数据模型
class newsModel(models.Model):
    newstitle = models.CharField(max_length=100)
    newscon = models.CharField(max_length=400)
    class Meta:#创建数据表
        db_table="newstable"

# 创建登录用户名
class enterModel(models.Model):
    id = models.AutoField(primary_key=True)
    xingming = models.CharField(max_length=8)
    xuehao = models.CharField(max_length=4,unique=True)
    dianhua = models.CharField(max_length=11)
    mima = models.CharField(max_length=12)
    gender = models.CharField(max_length=4)
    jianjie = models.CharField(max_length=100)
    # src = models.FileField(upload_to="images")
    class Meta:
        db_table = "entertable"

class enteriModel(models.Model):
    id = models.AutoField(primary_key=True)
    xingming = models.CharField(max_length=8)
    xuehao = models.CharField(max_length=4,unique=True)
    dianhua = models.CharField(max_length=11)
    mima = models.CharField(max_length=12)
    gender = models.CharField(max_length=4)
    jianjie = models.CharField(max_length=100)
    src = models.FileField(upload_to="images")
    class Meta:
        db_table = "enteritable"

