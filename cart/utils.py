from django.shortcuts import  get_object_or_404

from products.models import Product
from programs.models import Program
from profiles.models import Subscription

def get_item_from_item_id(item_id):
    try:
        # Check if item_id exists in Product
        if Product.objects.filter(pk=item_id).exists():
            item = get_object_or_404(Product, pk=item_id)
            return item
            
        # Check if item_id exists in Model2
        elif Program.objects.filter(pk=item_id).exists():
            item = get_object_or_404(Program, pk=item_id)
            return item
        # Check if item_id exists in Model3
        elif Subscription.objects.filter(pk=item_id).exists():
            item = get_object_or_404(Subscription, pk=item_id)
            return item
        else:
            # If item_id doesn't exist in any model
            return None
    except Exception as e:
        # Handle exceptions such as database connection errors
        print("An error occurred:", e)
        return None


def get_model_from_id(item_id):
    try:
        # Check if item_id exists in Product
        if Product.objects.filter(pk=item_id).exists():
            return Product
            
        # Check if item_id exists in Model2
        elif Program.objects.filter(pk=item_id).exists():
            return Program
        # Check if item_id exists in Model3
        elif Subscription.objects.filter(pk=item_id).exists():
            return Subscription
        else:
  
            return None
    except Exception as e:
        # Handle exceptions such as database connection errors
        print("An error occurred:", e)
        return None