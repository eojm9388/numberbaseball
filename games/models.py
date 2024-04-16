from django.db import models

# Create your models here.
class Player(models.Model):
    nickname1 = models.CharField(max_length=20)
    number1 = models.CharField(max_length=4)
    expect1 = models.CharField(max_length=4)
    nickname2 = models.CharField(max_length=20)
    number2 = models.CharField(max_length=4)
    expect2 = models.CharField(max_length=4)