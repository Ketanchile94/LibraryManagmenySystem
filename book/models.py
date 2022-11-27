from django.db import models
from book.manager import CustomManager

# Create your models here.

class Books(models.Model):
    books_category=(('non-fiction','Non-Fiction'),('edited','Edited'),('reference','Reference'),('fiction','Fiction'))
    book_name =models.CharField(max_length=30)
    author_name=models.CharField(max_length=30)
    price=models.IntegerField()
    Type_of_Book=models.CharField(max_length=20, choices=books_category)
    is_deleted = models.CharField(max_length = 2, default = 'n')

    #customObjects = models.Manager()
    myObjects = CustomManager()

class Contact(models.Model):
    username= models.CharField(max_length=30)
    email= models.EmailField(max_length=50)
    phone= models.CharField(max_length=13)
    desc= models.TextField()

    


  