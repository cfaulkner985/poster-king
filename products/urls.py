from django.urls import path
from django.conf.urls import url, include, handler404, handler500
from . import views

""" Paths to each page on the site """
urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]

handler404 = views.handler404
handler500 = views.handler500
