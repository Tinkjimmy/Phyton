from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book 

class BookListView(ListView):           #class-based view
   model = Book                         #specify model
   template_name = 'books/main.html' 

class BookDetailView(DetailView):
   model = Book
   template_name = 'books/detail.html'
