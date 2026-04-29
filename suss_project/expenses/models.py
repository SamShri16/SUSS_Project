from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    source = models.CharField(max_length=100)
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"