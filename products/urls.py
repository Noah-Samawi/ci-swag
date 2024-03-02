"""Products URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('', views.AddProductPage.as_view(), name='add_product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
