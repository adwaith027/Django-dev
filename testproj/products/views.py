from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import product
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.

def addProduct(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = ProductForm()
    return render(request,'ProductAdd.html',{'form':form})

def viewProduct(request):
        data=product.objects.all()
        return render (request,'ProductDisplay.html',{'data':data})

def updateProduct(request,id):
    pid=product.objects.get(pk=id)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=pid)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form=ProductForm(instance=pid)
    return render(request,'ProductUpdate.html',{'form':form})

def deleteProduct(request,id):
    pid=product.objects.get(pk=id)
    if request.method=='POST':
        product.delete(pid)
        return redirect('view')
    return render(request,'ProductDelete.html',{'pid':pid})

def listing(request):
    productlisting=product.objects.all()
    paginator=Paginator(productlisting,3)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'ProductListing.html',{'page_obj':page_obj})

def pageVisit(request):
    count = request.session.get('page_count',0)
    count += 1
    request.session['page_count']=count
    return render(request,'PageVisit.html',{'count':count})