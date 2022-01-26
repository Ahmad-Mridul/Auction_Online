from django.http import HttpResponse
from django.shortcuts import render
from Core.models import *


def index(request):

    productData=Product.objects.all()
    categorysData = Categories.objects.all()

    context = {
        'categorys': categorysData,
        'products':productData
    }

    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')
