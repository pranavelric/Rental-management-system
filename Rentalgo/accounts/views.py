from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from . import forms
# Create your views here.

class signup(CreateView):
    form_class = forms.UserForm
    success_url = 'accounts/login.html'
    template_name = 'accounts/signup.html'
    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = self.form_class()
            return render(request,self.template_name, {'form':form})

    def post(self,request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            auth.login(request,user)
            return redirect('home')
        return render(request,self.template_name, {'form':form})

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'error':'Incorrect username or password','login_form':LoginForm})
        else:
            return render(request, 'accounts/login.html', {'error':'Invalid Form','login_form':LoginForm})
    elif not request.user.is_authenticated:
        return render(request, 'accounts/login.html', {'login_form':LoginForm})
    else:
        return redirect('home')

@login_required
def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
