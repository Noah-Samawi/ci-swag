"""Profile views."""

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Subscription

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
