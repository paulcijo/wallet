from django.db import models
import datetime

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('C', 'Credit'),
        ('D', 'Debit'),
    )
    cost = models.FloatField()
    item = 	models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES, default=TRANSACTION_TYPE_CHOICES[1][0])
    necessary = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    