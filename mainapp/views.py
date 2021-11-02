from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
import os

from django.template.loader import render_to_string

from baskets.models import Basket
from baskets.views import basket_add, basket_remove
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

@login_required
def products(request, category_id=None, page_id=1):

    products = Product.objects.filter(category_id=category_id).select_related('category') if category_id !=None \
        else Product.objects.all().select_related('category')

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }

    return render(request, 'mainapp/products.html',context)

@login_required
def default_filter(request, page_id=1):

    products = Product.objects.all()

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }

    return render(request, 'mainapp/products.html',context)

@login_required
def product_add(request, product_id, wtd):
    if request.is_ajax():
        if wtd == 'Отправить в корзину':
            basket_add(request, product_id=product_id)
        elif wtd == 'Удалить из корзины':
            basket_remove(request, product_id=product_id)
        context = {
            'title': 'GeekShop - Каталог',
            'products': Product.objects.all(),
            'baskets': Basket.objects.filter(user=request.user).values('product_id'),
        }

        result = render_to_string('mainapp/goods.html', context)
        return JsonResponse({'result': result})