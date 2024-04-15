from django.db import models

# Create your models here.
class Player1(models.Model):
    nickname = models.CharField(max_length=20)
    number = models.IntegerField()
    expect = models.IntegerField()

class Player2(models.Model):
    nickname = models.CharField(max_length=20)
    number = models.IntegerField()
    expect = models.IntegerField()