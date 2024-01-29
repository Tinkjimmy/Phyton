from django.shortcuts import render
from django.contrib.auth.decorators import login_required  #decorator required for function-based views
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_bookname_from_id, get_chart




# Create your views here.
def home(request):
    return render(request,'sales/home.html')

@login_required  #adding the decorator to login-protect the view


def records(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None #inztialize dataframe to none
    book_title= None
    chart = None

    #check if button is clicked
    if request.method == 'POST':
        #READ book_title anc chart_type
        book_title= request.POST.get('book_title')
        chart_field = request.POST.get('chart_field')
        

    #to access a foreign key(book_name from the Book model) i add 2 underscores
    qs =Sale.objects.filter(book__name=book_title)
    
    if qs : #if data found convert the queryset values to pandas fataframe
        sales_df= pd.DataFrame(qs.values())
        
        #convert the ID to the name of the book
        #Book model has a __str__ method that returns the book name, Pandas will use that method to represent the Book object as a string.
        sales_df['book_id']=sales_df['book_id'].apply(get_bookname_from_id)
        chart=get_chart(chart_field, sales_df, labels=sales_df['date_created'].values)
        sales_df=sales_df.to_html()
    
    #pack up data to be sent to template in the context dictionary
    context={
        'form': form,
        'sales_df': sales_df,
        'chart': chart,
    }
    return render(request, 'sales/records.html',context)



