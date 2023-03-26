from django.db import models

# Create your models here.

class dados(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    Cpf = models.CharField(max_length=20)
    createdAt = models.DateField(auto_now_add=True)
    Active = models.BooleanField(default=True)
