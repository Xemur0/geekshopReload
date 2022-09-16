from django.urls import path
from admins.views import index, UserListView, UserUpdateView, UserCreateView, UserDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, OrderView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

# import baskets.views as basket

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_user_delete'),

    path('category/', CategoryListView.as_view(), name='admins_category'),
    path('category-create/', CategoryCreateView.as_view(), name='admins_category_create'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admins_category_update'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admins_category_delete'),

    path('orders/', OrderView.as_view(), name='orders'),
    path('product/', ProductListView.as_view(), name='admin_product'),
    path('product-create/', ProductCreateView.as_view(), name='admins_product_create'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='admins_product_update'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='admins_product_delete'),
]
