from django.urls import path
from book import views

urlpatterns = [
    path('addbook/',views.add),
    path('viewbook/',views.display),
    path('updatebook/<int:did>', views.updatebook),
    path('delete/<int:did>', views.delete),
    path('register/', views.registeruser, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('upcomingbook/', views.upcomingbook),
    path('updatebook/<str:id>', views.search, name='search'),
    path('contact/', views.contactus),
    path('about/', views.aboutus),
    path('htol/', views.htol),
    path('ltoh/', views.ltoh),
    path('AtoZ/', views.AtoZ),
    path('ZtoA/', views.ZtoA),
    path("AatoZz/",views.AatoZz),
    path("ZztoAa/",views.ZztoAa),
    path('lowtohigh/',views.lowtohigh),
    path('hightolow/',views.hightolow),
    path('CAtoZ/',views.CAtoZ),
    path('CZtoA/',views.CZtoA),
    path('catfilter/<str:cat>',views.catfilter)
]