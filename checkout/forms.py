"""Checkout Forms"""

from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for collecting user information for placing an order.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget = PhoneNumberPrefixWidget()

    class Meta:
        """
        Metadata for the OrderForm.
        """

        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county', 'user_profile',)
