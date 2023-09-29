from django.db import models


class Cat(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    cyes = models.CharField(max_length=100)
    ears = models.TextField()
    tail = models.TextField()
