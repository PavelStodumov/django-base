from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product
from basketapp.models import Basket

import random
# Create your views here.

main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products:products_index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


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
        'products': Product.objects.all()[:2]
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'main_menu': main_menu
    }
    return render(request, 'mainapp/contact.html', content)


def products_index(request):

    basket = get_basket(request.user)

    value_basket = sum(map(lambda b: b.value(), basket))
    price_basket = sum(map(lambda b: b.price(), basket))

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    category_all_products = {'name': 'все', 'id': 9999}
    categories = [category_all_products,
                  *ProductCategory.objects.all()]
    products = Product.objects.all()

    content = {
        'title': 'Продукты',
        'main_menu': main_menu,
        'product_categories': categories,
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
        'value_basket': value_basket,
        'price_basket': price_basket,
    }
    return render(request, 'mainapp/products.html', content)


def products(request, pk=None):

    basket = get_basket(request.user)

    value_basket = sum(map(lambda b: b.value(), basket))
    price_basket = sum(map(lambda b: b.price(), basket))

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    category_all_products = {'name': 'все', 'id': 9999}
    categories = [category_all_products,
                  *ProductCategory.objects.all()]
    all_products = Product.objects.all()
    selected_category = ProductCategory.objects.filter(id=pk)
    products = Product.objects.all()
    # навоял какой-то костыль с id категории всех товаров. с id=0 не получается. открывается страница горячего предложения, почему - не понимаю. Думаю поставить id=1, а в модели, в поле id как-нибудь запретить присваивать единицу. Или посоветуйте как лучше сделать
    if pk:
        if pk == 9999:
            selected_category = category_all_products
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category_id=pk)
            selected_category = get_object_or_404(ProductCategory, id=pk)

    content = {
        'title': 'Продукты',
        'main_menu': main_menu,
        'product_categories': categories,
        'products': products,
        'selected_category': selected_category,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
        'value_basket': value_basket,
        'price_basket': price_basket,
    }

    return render(request, 'mainapp/category.html', content)


def product(request, pk):
    product = Product.objects.filter(id=pk)

    content = {
        'main_menu': main_menu,
        'title': product[0].name,
        'categories': ProductCategory.objects.all(),
        'product': product[0],
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)
