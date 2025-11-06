from django.db import models

# Create your models here.

class menu(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.CharField(max_length=7)

    def __str__(self):
        return self.name