from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 50)
    description = models.TextField()
