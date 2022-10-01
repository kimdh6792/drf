from django.urls import path
from restframework.views import BuyListAPI

urlpatterns = [
    path('buy/', BuyListAPI.as_view())
]