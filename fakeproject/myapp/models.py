from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    job = models.CharField(max_length=100)
