from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
