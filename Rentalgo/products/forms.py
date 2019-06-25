from django import forms
from django.contrib.auth.models import User
from .models import Product

class ProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('prod_name','description','img1','img2','dprice','wprice','mprice','available_for_selling','sprice')
        labels = {
                    'prod_name': 'Product Name',
                    'description': 'Description',
                    'img1': 'Image 1',
                    'img2': 'Image 2',
                    'dprice': 'Rent per Day',
                    'wprice': 'Rent per Week',
                    'mprice': 'Rent per Month',
                    'sprice': 'Selling Price(Fill if available for sale)',
        }
