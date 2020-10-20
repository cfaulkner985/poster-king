from django.urls import path
from django.conf.urls import url, include, handler404, handler500
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]

handler404 = views.handler404
handler500 = views.handler500