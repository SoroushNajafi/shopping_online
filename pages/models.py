from django.db import models


class Subscribe(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
