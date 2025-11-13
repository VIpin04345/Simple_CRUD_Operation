from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    age=models.IntegerField()
    city=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name