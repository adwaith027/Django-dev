from . import views
from django.urls import path

urlpatterns=[
    path('create/',views.addProduct,name='create'),
    path('view/',views.viewProduct,name='view'),
    path('update/<int:id>/',views.updateProduct,name='update'),
    path('delete/<int:id>/',views.deleteProduct,name='delete'),
    path('listing/',views.listing,name='listing'),
    path('visitcount/',views.pageVisit,name='visit'),
    path('pdf/<int:pk>/', views.getpdf, name='getpdf'),
    path('email/<int:pk>/', views.getmail, name='getmail'),
]