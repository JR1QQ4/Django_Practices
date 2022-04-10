from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class USER(models.Model):
    '''自定义USER表对应的Model类'''
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    password = models.CharField()
    email = models.CharField()

    def __str__(self) -> str:
        return "%d, %s, %s, %s" % (self.id, self.name, self.password, self.email)
    
    # 自定义对应的表名，默认表名: myapp_user
    class Meta:
        db_table = "USER"