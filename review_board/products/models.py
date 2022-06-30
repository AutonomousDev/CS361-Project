from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField()
    brand = models.charField()
    description = models.TextField()
