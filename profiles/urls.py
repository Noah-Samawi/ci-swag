from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('subscriptions', views.SubscriptionsView.as_view(), name='subscriptions'),
    path('remove_subscription',views.remove_subscription, name='remove_subscription'),
]
