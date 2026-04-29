from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField()


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    source = models.CharField(max_length=100)
    date = models.DateField()