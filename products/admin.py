from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category model.

    Defines the display fields for the Category admin panel.
    """
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Category, CategoryAdmin)