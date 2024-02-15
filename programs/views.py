"""Program Views"""

from django.shortcuts import render, get_object_or_404
from .models import Program

from products.utils import filter_and_sort_products




# Create your views here.
def all_programs(request):
    """ A view to show all programs, including sorting and search queries """
    programs = Program.objects.all()

    filtered_products, query, categories, sort, direction, category = \
        filter_and_sort_products(products=programs, request=request)

    context = {
        'programs': filtered_products,
        'search_term': query,
        'current_categories': categories,
        'sort': sort,
        'direction': direction,
        'query': query,
        'category': category
    }

    return render(request, 'programs/programs.html', context)



def program_detail(request, program_id):
    """ A view to show individual program details """

    program = get_object_or_404(Program, pk=program_id)

    context = {
        'program': program,
    }

    return render(request, 'programs/program_detail.html', context)
