from django.urls import path
from django.conf.urls import url, include, handler404, handler500
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]

handler404 = views.handler404
handler500 = views.handler500
