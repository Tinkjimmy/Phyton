from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book 
from django.contrib.auth.mixins import LoginRequiredMixin #this libary is required to protect a class-based view


class BookListView(LoginRequiredMixin,ListView):           #class-based view
   model = Book                         #specify model
   template_name = 'books/main.html' 

class BookDetailView(LoginRequiredMixin,DetailView):
   model = Book
   template_name = 'books/detail.html'
