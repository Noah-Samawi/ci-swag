from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('subscriptions', views.SubscriptionsView.as_view(), name='subscriptions'),
    path('remove_subscription',views.remove_subscription, name='remove_subscription'),
]
