from django.db import models

# Create your models here.t

class Employee(models.Model):

    first_name = models.CharField(max_length=120)
    last_name =  models.CharField(max_length=120)
