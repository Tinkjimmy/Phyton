from django.urls import path,include
from .views import home,records

app_name= 'sales'

urlpatterns = [
    path('',home),
    path('sales/', records, name='records'), 
]