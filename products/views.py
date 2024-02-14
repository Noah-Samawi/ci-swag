"""Product Views"""

from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
