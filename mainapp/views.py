from django.shortcuts import render
import os,json

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):

    context = {
        'title': 'geekshop',
        'categories': ProductCategory.objects.all(),
        'products':Product.objects.all()
    }
    return render(request, 'mainapp/products.html',context)