from django.urls import path
from login import views

app_name = "login"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name='user_login'),
    path('icon/', views.icon, name='icon')
    
]