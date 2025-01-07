
from django.urls import path
from api import views


urlpatterns = [
    path('', views.simpleapi),
    path('signupapi', views.signup),
    path('loginapi', views.login),
    path('logoutapi', views.logout_user),
    

]