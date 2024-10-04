from django.db import models

# Create your models here.
class Student(models.Model):
    SID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mobile =models.BigIntegerField(max_length=12)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.TextField()

def __str__(self):
    return f"Book ID: {self.SID} Name:{self.name}"