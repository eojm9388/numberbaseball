from django.db import models

# Create your models here.
class Player1(models.Model):
    nickname = models.CharField(max_length=20)
    number = models.CharField(max_length=4)
    
class Player2(models.Model):
    nickname = models.CharField(max_length=20)
    number = models.CharField(max_length=4)


class Expect1(models.Model):
    player = models.ForeignKey(Player1, on_delete=models.CASCADE)
    expect = models.CharField(max_length=4)
    status = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

class Expect2(models.Model):
    player = models.ForeignKey(Player2, on_delete=models.CASCADE)
    expect = models.CharField(max_length=4)
    status = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

