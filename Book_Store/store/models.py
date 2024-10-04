from django.db import models

# Create your models here.

class Message(models.Model):
    mobile = models.BigIntegerField(max_length=12)
    message = models.TextField()

class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=150)
    date = models.DateField(verbose_name='Publish Date')
    summary = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    
def __str__(self):
    return f"Book ID: {self.bid} Name:{self.name}"