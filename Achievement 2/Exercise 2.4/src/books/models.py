from django.db import models
from django.urls import reverse

book_types=(('hc','Hard cover'),('eb','E-Book'),('ab','Audiobook'))
genre_choices= (('cl','Classic'),('ro','Romantic'),('co','Comic'),('fa','Fantasy'),('ho','Horror'),('ed','Educational'))
# Create your models here.
class Book(models.Model):
   
    name=models.CharField(max_length=120)
    
    genre =models.CharField(max_length=12,choices=genre_choices,default='classic')
    book_type =models.CharField(max_length=12,choices=book_types ,default='hardcopy')
    price=models.FloatField(help_text= 'inUS dollars $')
    author_name= models.CharField(max_length=120)
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)       
    def get_absolute_url (self):
        return reverse ('books:detail', kwargs={'pk': self.pk})


























