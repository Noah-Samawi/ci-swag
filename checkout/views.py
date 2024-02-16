"Checkout Views"
import stripe
import json
import inspect


from django.shortcuts import render, redirect, reverse
from django.views import View
from django.conf import settings
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from profiles.models import UserProfile
from cart.contexts import cart_contents
from cart.utils import get_item_from_item_id


from products.models import Product
from programs.models import Program
from profiles.models import Subscription

from .models import Order, OrderLineItem
from .forms import OrderForm



# Create your views here.
class CheckoutView(View):
    template_name = 'checkout/checkout.html'
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_wh_key = settings.STRIPE_WH_SECRET

    def get(self, request, *args, **kwargs):
        current_cart = cart_contents(request)
        total = current_cart['total']

        if len(current_cart['cart_items']) == 0:
            messages.error(request, "There are no items in your cart")
            return redirect(reverse('view_cart'))

        stripe_total = round(total * 100)

        if request.user.is_authenticated:
            try:
                profile=UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not self.stripe_secret_key:
            return redirect(reverse('home'))


        stripe.api_key = self.stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            'order_form': order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        profile = None

        form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'country': request.POST['country'],
                'postcode': request.POST['postcode'],
                'town_or_city': request.POST['town_or_city'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
                'county': request.POST['county'],
            }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            # Add user profile to order if user is authenticated
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                order.user_profile = profile

            # Add stripe pid and original cart to order
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.original_cart = json.dumps(cart)
            order.stripe_pid = pid

            order.save()

            for item_id, item_data in cart.items():
                # Membership discount
                discount = 0
                item =  get_item_from_item_id(item_id)
                try:
                    if isinstance(item, Subscription):
                        content_type = ContentType.objects.get_for_model(Subscription)
                        if request.user.is_authenticated:
                            request.user.profile.active_subscription = item
                            request.user.profile.save()
                    elif isinstance(item, Program):
                        content_type = ContentType.objects.get_for_model(Program)
                        if request.user.is_authenticated:
                            if request.user.profile.subscription:
                                discount = request.user.profile.subscription.program_discount
                    else:
                        content_type = ContentType.objects.get_for_model(Product)
                        if request.user.is_authenticated:
                            if request.user.profile.subscription:
                                discount = request.user.profile.subscription.product_discount


                    order_line_item = OrderLineItem(
                            order=order,
                            content_type=content_type,
                            object_id=item_id,
                            quantity=item_data,
                            subscription_discount=discount
                        )
                    order_line_item.save()


                except item.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            if request.user.is_authenticated:
                if request.user.profile.subscription:
                    request.user.profile.subscription = None
                    request.user.profile.save()

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse('checkout'))

        # If form is invalid, store form data in session and redirect to checkout
        order_form_data = {
                        'cleaned_data': order_form.cleaned_data,
                        'errors': order_form.errors,
                    }

        request.session['order_form_data'] = order_form_data

        messages.error(request, 'There was an error with your form. \
            Please double-check your information.')
        return redirect(reverse('checkout'))



@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
