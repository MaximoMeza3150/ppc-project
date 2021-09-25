from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    path('', views.feed , name='feed'),
    path('register/' , views.register , name='register'),
    path('login/' , LoginView.as_view(template_name='control_de_pendientes/login.html') , name='login'),
    path('logout/' , LogoutView.as_view(template_name='control_de_pendientes/logout.html') , name='logout'),
]