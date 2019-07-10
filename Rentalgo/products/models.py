from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    prod_name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=False)
    quantity = models.PositiveIntegerField(default=1, blank=False)
    dprice = models.PositiveIntegerField()
    wprice = models.PositiveIntegerField()
    mprice = models.PositiveIntegerField()
    img1 = models.ImageField(upload_to='images/',null=True)
    img2 = models.ImageField(upload_to='images/',null=True)
    owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='products')
    selling_choice = [
        ('y','YES'),
        ('n','NO'),
    ]
    available_for_selling = models.CharField(max_length=1, choices=selling_choice, default='n')
    sprice = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.prod_name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='iorder')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myorder')
    address = models.CharField(max_length=512, blank=False)
    city = models.CharField(max_length=64, blank=False)
    zip_code = models.PositiveIntegerField()
    contact = models.CharField(max_length=10, blank=False)
    order_date = models.DateField()
    date_range = models.CharField(max_length=128,blank=False)
    cost = models.PositiveIntegerField(null=True)

class BuyOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='buyorder')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyiorder')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buymyorder')
    address = models.CharField(max_length=512, blank=False)
    city = models.CharField(max_length=64, blank=False)
    zip_code = models.PositiveIntegerField()
    contact = models.CharField(max_length=10, blank=False)
    order_date = models.DateField()
    cost = models.PositiveIntegerField(null=True)
