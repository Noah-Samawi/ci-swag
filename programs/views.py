from django.shortcuts import render
from .models import Program



# Create your views here.
def all_programs(request):
    """ A view to show all programs, including sorting and search queries """
    programs = Program.objects.all()

    context = {
        'programs': programs,

    }

    return render(request, 'programs/programs.html', context)
