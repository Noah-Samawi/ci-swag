from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
