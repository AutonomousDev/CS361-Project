from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    product_image = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{},- {}'.format(self.name, self.brand)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    comments = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.product.pk})
