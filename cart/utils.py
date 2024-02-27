"""Utility functions for the cart app."""

from django.shortcuts import get_object_or_404

from products.models import Product
from programs.models import Program
from profiles.models import Subscription


def get_item_from_item_id(item_id):
    """Get the item from the item_id."""

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


def apply_subscription_discount(
                                subscription_discount,
                                product,
                                total_item_price):
    """
    Apply subscription discount to the product and calculate the total
    discount amount.
    """
    members_discount = 0

    if subscription_discount:
        discount_percentage = subscription_discount / 100
        discount_amount = product.total_final_price * discount_percentage
        total_discount_amount = total_item_price * discount_percentage
        total_item_price -= total_discount_amount
        product.discount = discount_amount
        members_discount += total_discount_amount

    return total_item_price, members_discount
