from django.db import models

# Create your models here.

# 자동매매 등록 사용자 DB
class Autotrade(models.Model):
    member_id = models.CharField(max_length=35,null=False,)
    member_access_key = models.CharField(max_length=200, null=False)
    member_secret_key = models.CharField(max_length=200, null=False)


# 자동매매 거래 내역
class Autotrade_list(models.Model):
    member_id = models.CharField(max_length=35, null=False)
    side = models.CharField(max_length=30, null=False)
    price = models.CharField(max_length=30, null=True)
    created = models.CharField(max_length=100, null=False)
    volume = models.CharField(max_length=30, null=True)