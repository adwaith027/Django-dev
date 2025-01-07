from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
    path('create/', views.create_product),
    path('retrieve/', views.retrieve_product),
    path('edit/<int:pk>', views.update_product),
    path('delete/<int:pk>', views.delete_product),

]