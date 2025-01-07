from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/retrieve')
    else:
        form = ProductForm()    
    return render(request,'create.html',{'form':form})

@login_required(login_url='/login/')
def retrieve_product(request):
    product_list = Product.objects.all()  # Replace with your query if needed

    # Set up pagination
    paginator = Paginator(product_list, 3)  # Show 10 products per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)

    return render(request, 'retrieve.html', {'page_obj': page_obj})



def update_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products/retrieve')
    else:
        form =ProductForm(instance=product)
    return render(request,'update.html',{'product':product,'form':form})



def delete_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
            product.delete()
            return redirect('/products/retrieve')
        
    return render(request,'delete.html',{'product':product})


