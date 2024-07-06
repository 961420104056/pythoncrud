from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    job=models.CharField(max_length=100)
    salary=models.IntegerField()


# Create your models here.
