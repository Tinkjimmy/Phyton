from django.urls import path,include
from .views import home

app_name= 'sales'

urlpatterns = [
    path('',home),
    
]