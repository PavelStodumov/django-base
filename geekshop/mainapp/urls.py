from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products_index, name='products_index'),
    path('category/<int:pk>', mainapp.products, name='products'),
    path('product/<int:pk>', mainapp.product, name='product')
]
