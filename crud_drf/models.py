from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name


class User(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    user_email = models.EmailField(null=False)
    