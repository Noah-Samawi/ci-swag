"""Product Views"""

from django.shortcuts import render
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    category = ''
    sort = None
    direction = 'asc'

    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            category = request.GET['category']

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            query = ''
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    context = {
        'products': products,
        'current_categories': categories,
        'category': f"{category} products",
        'sort': sort,
        'direction': direction,
        'query': query
    }

    return render(request, 'products/products.html', context)
