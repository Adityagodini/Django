from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5,decimal_places=2)
    email = models.EmailField()


    def __str__(self):
        return self.name