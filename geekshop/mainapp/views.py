from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product
from basketapp.models import Basket

import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products:products_index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]
categories = [{'name': 'все', 'id': 0},
              *ProductCategory.objects.all()]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category)[:3]
    return same_products


def index(request):
    content = {
        'title': 'главная',
        'main_menu': main_menu,
        'products': Product.objects.all()[:2],
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'main_menu': main_menu,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', content)


def products_index(request):

    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    products = Product.objects.all()

    content = {
        'title': 'Продукты',
        'main_menu': main_menu,
        'product_categories': categories,
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)


def products(request, pk=None, page=1):

    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    selected_category = ProductCategory.objects.filter(id=pk)
    products = Product.objects.all()

    if pk is not None:
        if pk == 0:
            selected_category = categories[pk]
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category_id=pk)
            selected_category = get_object_or_404(ProductCategory, id=pk)
            
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': 'Продукты',
        'main_menu': main_menu,
        'product_categories': categories,
        'products': products_paginator,
        'selected_category': selected_category,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    
    return render(request, 'mainapp/category.html', content)


def product(request, pk):
    product = Product.objects.filter(id=pk)

    content = {
        'product_categories': categories,
        'main_menu': main_menu,
        'title': product[0].name,
        'categories': ProductCategory.objects.all(),
        'product': product[0],
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)
