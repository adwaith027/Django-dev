from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test

def usignup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ulogin')
    else:
        form=UserCreationForm()
    return render(request,'usignup.html',{'form':form})

def user_check(user):
    return user.username.endswith('@example.com')

def ulogin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'ulogin.html',{'form':form})

@login_required(login_url='/ulogin/')
def ulogout(request):
    if request.method=='POST':
        logout(request)
        return redirect('ulogin')
    return render(request, 'ulogout.html', {'user':request.user})

@login_required(login_url='/ulogin/')
def home(request):
    return render(request,'home.html')

@login_required(login_url='/ulogin/')
@user_passes_test(user_check,login_url='/ulogin/')
def about(request):
    return render(request,'about.html')

@login_required(login_url='/ulogin/')
def listUser(request):
    user=User.objects.all()
    return render (request,'userlisting.html',{'user':user})