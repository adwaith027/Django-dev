from django.urls import path
from . import views


urlpatterns=[
    path('simpleapi/',views.simpleapi,name='simpleapi'),
    path('signup/',views.signup,name='signup_api'),
    path('login/', views.login, name='login_api'),
    path('createproduct/',views.createProduct,name='createProduct'),
]