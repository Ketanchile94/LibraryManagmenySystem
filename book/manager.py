from django.db import models

class CustomManager(models.Manager):

    def desc_by_bookname_bn(request):
        return super().order_by('-book_name')

