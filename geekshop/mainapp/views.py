from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.

# контент у меня получается общий для всего сайта. Наверное это не очень хорошо
content = {
    'product_title': 'продукты',
    'main_title': 'магазин',
    'links_menu': [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ],
    'main_menu': [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
    'same_products': [
        {'img': "/static/img/product-11.jpg"},
        {'img': "/static/img/product-21.jpg"},
        {'img': "/static/img/product-31.jpg"}
    ],
    'products': Product.objects.all()[:],
    # не придумал как сделать категорию, объединяющую все категории.
    'product_categories': [{'name': 'все'}, *ProductCategory.objects.all()[2:]],
}


def index(request):
    return render(request, 'mainapp/index.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', content)


def products(request, pk=None):
    print(pk)
    if pk == '':
        return render(request, 'mainapp/products.html', content)
