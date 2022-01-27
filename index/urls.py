from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from auction import settings
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('auction/', views.auction, name='auction'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




