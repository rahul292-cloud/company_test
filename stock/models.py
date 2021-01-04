from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name=models.CharField(max_length=100,null=True,blank=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.tag_name

class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_name=models.CharField(max_length=100,null=False,blank=False)
    product_image=models.FileField(upload_to='product_image', null=True, blank=True)
    tags=models.ManyToManyField(Tag, blank=True)
    description=models.CharField(max_length=250,null=True,blank=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name