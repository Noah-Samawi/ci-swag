"""Profile views."""

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Subscription, UserProfile
from .forms import UserProfileForm, UpdateUserForm



class ProfileView(LoginRequiredMixin, View):
    """
    View for displaying and updating user profiles.

    """
    template_name = 'profiles/profile.html'
    user_form_class = UpdateUserForm
    profile_form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        """
        Retrieves context data for rendering the profile update page.
        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """
        user = self.request.user
        profile = get_object_or_404(UserProfile, user=user)
        orders = profile.orders.all()

        for order in orders:
            order.total_items = 0
            for line_item in order.lineitems.all():
                order.total_items += line_item.quantity

        context = {
            "user_form": kwargs.get("user_form",
                                    self.user_form_class(instance=user)),
            "profile_form": kwargs.get(
                "profile_form", self.profile_form_class(instance=profile)
            ),
            'orders': orders,
            'on_profile_page': True,

        }
        return context

    def get(self, request):
        """
        Handles HTTP GET requests for rendering the profile update page.

        """
        context = self.get_context_data()
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        """
        Handles HTTP POST requests for updated the profile models in database.

        """
        context = self.get_context_data()
        profile = get_object_or_404(UserProfile, user=request.user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)


        if "user_form" in request.POST:
            if user_form.is_valid():
                user_form.save()
                context["user_form"] = user_form
            else:
                context['user_form'] = user_form
                return render(request, self.template_name, context)
        else:
            if profile_form.is_valid():
                profile_form.save()
                context["profile_form"] = profile_form
            else:
                context["profile_form"] = profile_form

        return render(request, self.template_name, context)




class SubscriptionsView(LoginRequiredMixin, View):
    """
    View for displaying user subscriptions.

    """

    template_name = 'profiles/subscriptions.html'


    def get(self, request):
        """
        Retrieves all subscriptions from the database and orders them by price.
        If the current user has an active subscription, marks the corresponding
        subscription as 'current' in the context.
        
        """
        subscriptions = Subscription.objects.all().order_by('price')
        if request.user.profile.active_subscription:
            for subscription in subscriptions:
                if subscription.id == request.user.profile.active_subscription.id:
                    subscription.current = True
                else:
                    subscription.current = False

        context = {
            'subscriptions': subscriptions,
        }

        return render(request, self.template_name, context)


def remove_subscription(request):
    """Remove a user's active subscription."""

    redirect_url = request.POST.get('redirect_url')

    try:
        messages.success(request, f'Your {request.user.profile.active_subscription.name} membership was cancelled')
        request.user.profile.active_subscription = None
        request.user.profile.subscription = None
        request.user.profile.save()
        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error unsubscribing your membership: {e}')
        return HttpResponse(status=500)
