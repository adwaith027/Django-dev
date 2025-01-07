from django.urls import path
from . import views


urlpatterns=[
    path('simpleapi/',views.simpleapi,name='simpleapi'),
    path('signup/',views.signup,name='signup_api'),
    path('login/', views.login, name='login_api'),
    path('createproduct/',views.createProduct,name='createProduct_api'),
    path('listproduct/',views.listProduct,name='listProduct_api'),
    path('updateproduct/<int:pk>/', views.updateProduct, name='updateProduct_api'),
]