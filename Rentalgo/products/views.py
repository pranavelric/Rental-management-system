from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from .forms import ProdForm
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products':products})

@login_required
def create(request):
    if request.method == 'POST':
        prod_form = ProdForm(request.POST,request.FILES)
        if prod_form.is_valid():
            product = prod_form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            print (prod_form.errors)
            return render(request, 'products/create.html', {'prod_form':ProdForm})

    else:
        if request.user.profile.kyc_verified == "n":
            return render(request, 'products/home.html', {'error':'Verify your kyc before posting an AD!'})
        else:
            prod_form = ProdForm
            return render(request, 'products/create.html', {'prod_form':prod_form})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})
