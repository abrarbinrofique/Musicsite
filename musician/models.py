from django.db import models

# Create your models here.

class Musician(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=30)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Instrument=models.CharField(max_length=20)

    def __str__(self):
        return self. Firstname