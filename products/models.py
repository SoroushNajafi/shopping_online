from django.db import models
from django.urls import reverse


class Product(models.Model):
    CATEGORIES_CHOICES = (
        ('women', 'women'),
        ('men', 'men'),
        ('kid', 'kid')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(max_length=200, blank=True)
    categories = models.CharField(choices=CATEGORIES_CHOICES, max_length=200, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



