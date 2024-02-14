"""Product Views"""

from django.shortcuts import render
from .models import Product

from .utils import filter_and_sort_products

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    filtered_products, query, categories, sort, direction, category = \
        filter_and_sort_products(products=products, request=request)

    context = {
        'products': filtered_products,
        'search_term': query,
        'current_categories': categories,
        'sort': sort,
        'direction': direction,
        'query': query,
        'category': category
    }

    return render(request, 'products/products.html', context)
