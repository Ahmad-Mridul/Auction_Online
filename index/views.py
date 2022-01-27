from django.http import HttpResponse
from django.shortcuts import render
from Core.models import *


def index(request):
    productData = Product.objects.all()
    categorysData = Categories.objects.all().order_by("id")[:6]
    context = {
        'categorys': categorysData,
        'products': productData
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def auction(request):
    # category =Categories.objects.get(slug=slug)
    # contex={
    #     'category':category
    # }
    return render(request, 'auction.html')
