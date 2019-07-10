from django import forms
from django.contrib.auth.models import User
from .models import Product, Order, BuyOrder
from django.forms.widgets import SelectDateWidget

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
# class UserProfileInfoForm(forms.ModelForm):
#     class Meta:
#         model = UserProfileInfo
#         fields = ('portfolio_site', 'profile_pic')

# add the form by seeing the above content and then delete the above content
class ProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('prod_name','description','img1','img2','quantity','dprice','wprice','mprice','available_for_selling','sprice')
        labels = {
                    'prod_name': 'Product Name',
                    'description': 'Description',
                    'quantity': 'Quantity',
                    'img1': 'Image 1',
                    'img2': 'Image 2',
                    'dprice': 'Rent per Day',
                    'wprice': 'Rent per Week',
                    'mprice': 'Rent per Month',
                    'sprice': 'Selling Price(Fill if available for sale)',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address','city','zip_code','contact','date_range',)
        labels = {
                    'date_range': 'Date Range',
                    'address': 'Address',
                    'city': 'City',
                    'zip_code': 'Zip Code',
                    'contact': 'Mobile Number',
        }

class BuyForm(forms.ModelForm):
    class Meta:
        model = BuyOrder
        fields = ('address','city','zip_code','contact',)
        labels = {
                    'address': 'Address',
                    'city': 'City',
                    'zip_code': 'Zip Code',
                    'contact': 'Mobile Number',
        }
