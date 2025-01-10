from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
from .models import product
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

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

def getpdf(request,pk):
    pdt = get_object_or_404(product,pk=pk)
    template = get_template('PdfGen.html')
    html = template.render({'pdt': pdt})
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)
    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(pdt.ProductName)
        return response
    

def getmail(request,pk):
    pdt=product.objects.get(pk=pk)
    subject = f"New Product: {pdt.ProductName}"
    from_email = "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]
    html_message = render_to_string('PdfMail.html', {'pdt': pdt})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return HttpResponse('Email sent successfully')