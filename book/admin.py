from django.contrib import admin
from book.models import Books, Contact
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display=('book_name','author_name','price','Type_of_Book')

class ContactAdmin(admin.ModelAdmin):
    list_display=('username','email','phone','desc')

admin.site.register(Books, BooksAdmin)
admin.site.register(Contact, ContactAdmin)