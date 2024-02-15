from django.urls import path
from . import views

urlpatterns = [
    path('subscriptions', views.SubscriptionsView.as_view(), name='subscriptions'),
]
