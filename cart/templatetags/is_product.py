"""Custom template tag for checking if a value is a product."""

from django import template
from products.models import Product

register = template.Library()

@register.filter(name='is_product')
def is_product(value):
    return isinstance(value, Product)