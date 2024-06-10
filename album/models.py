from django.db import models

from musician.models import Musician

import datetime

# Create your models here.

class Album(models.Model):
    Name=models.CharField(max_length=20)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True, default=datetime.date.today)

       
    RATINGS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    Rating = models.IntegerField(choices=RATINGS_CHOICES)





    def __str__(self):
        return self. Name
