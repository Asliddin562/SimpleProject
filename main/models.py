from unittest.mock import mock_open

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=15)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")


class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length = 15)
