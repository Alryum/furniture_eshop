from django.db import models
from django.urls import reverse

class Furniture(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='products_images/')
    size = models.CharField(max_length=100, blank=True)
    producer = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('detail_product', kwargs={'pk': self.pk})

