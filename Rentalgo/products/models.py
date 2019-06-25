from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    prod_name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=False)
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
