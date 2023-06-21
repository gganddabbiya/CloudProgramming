from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sex = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    age = models.IntegerField(max_length = 100,null=True)
    grade = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length=100)

    def get_phone_num(self):
        value = str(self.phone_number)
        return value[:3] + '-' + value[3:7] + '-' + value[7:]
