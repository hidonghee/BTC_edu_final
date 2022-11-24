from django.db import models

# Create your models here.


class Autotrade(models.Model):
    member_id = models.CharField(max_length=35,null=False,)
    member_access_key = models.CharField(max_length=200, null=False)
    member_secret_key = models.CharField(max_length=200, null=False)