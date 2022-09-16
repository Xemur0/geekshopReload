from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('category/<int:category_id>/', mainapp.products, name='category'),
   path('product_add/<int:product_id>/<str:wtd>/', mainapp.product_add, name='add_product'),
   path('page/<int:page_id>/', mainapp.products, name='page'),
   path('category/', mainapp.products, name='default_filter'),


]