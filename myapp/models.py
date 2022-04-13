from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    '''自定义USER表对应的Model类'''
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)

    def __str__(self) -> str:
        return "%d, %s, %s, %d, %s" % (self.id, self.username, self.password, self.age, self.email)
    
    # 自定义对应的表名，默认表名: myapp_user
    class Meta:
        db_table = "user_info"