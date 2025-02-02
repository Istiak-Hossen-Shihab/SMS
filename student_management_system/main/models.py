from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=14)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name