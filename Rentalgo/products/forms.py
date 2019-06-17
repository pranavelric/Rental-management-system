from django import forms
from django.contrib.auth.models import User
from .models import Product

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
        fields = ('prod_name','description','img1','img2','dprice','wprice','mprice','available_for_selling')
