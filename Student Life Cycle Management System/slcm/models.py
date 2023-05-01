from inspect import Attribute
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length = 20)
    reg_no = models.PositiveIntegerField(primary_key=True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.reg_no)
