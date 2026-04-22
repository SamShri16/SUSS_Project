from django.db import models

class Expense(models.Model):
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField()   # ✅ NEW

    def __str__(self):
        return f"{self.category} - {self.amount}"
    
class Income(models.Model):
    amount = models.FloatField()
    source = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.source} - {self.amount}"    