from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    CATEGORIES_CHOICES = (
        ('women', 'women'),
        ('men', 'men'),
        ('kids', 'kids'),
        ('extra', 'accessories')
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

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class ActiveCommentsManage(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManage, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='comment author',
                               )
    body = models.TextField(verbose_name='comment')
    stars = models.CharField(verbose_name='your score to this product', max_length=10, choices=PRODUCT_STARS)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManage()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
