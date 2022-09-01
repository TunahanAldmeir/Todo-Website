from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Toodo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='toodo')

    def __str__(self):
        return self.title