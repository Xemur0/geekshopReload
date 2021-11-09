from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import os

from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView

from baskets.models import Basket
from baskets.views import basket_add, basket_remove
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.cache import cache


MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
@cache_page(3600)
def index(request):
    return render(request, 'mainapp/index.html')


def get_link_category():
    if settings.LOW_CACHE:
        key = 'links_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()

def get_link_product():
    if settings.LOW_CACHE:
        key = 'links_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')

def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)




@login_required
def products(request, category_id=None, page_id=1):

    # products = Product.objects.filter(category_id=category_id).select_related('category') if category_id !=None \
    #     else Product.objects.all().select_related('category')

    products = get_link_product()

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
            'products': get_link_category(),
            'baskets': Basket.objects.filter(user=request.user).values('product_id'),
        }

        result = render_to_string('mainapp/goods.html', context)
        return JsonResponse({'result': result})

class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()

        context['product'] = get_product(self.kwargs.get('pk'))
        context['categories'] = ProductCategory.objects.all()
        return context