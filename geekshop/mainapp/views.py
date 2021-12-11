from django.shortcuts import render

# Create your views here.


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
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
    'same_products': [
        {'img': "/static/img/product-11.jpg"},
        {'img': "/static/img/product-21.jpg"},
        {'img': "/static/img/product-31.jpg"}
    ]
}


def index(request):
    return render(request, 'mainapp/index.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', content)


def products(request):
    return render(request, 'mainapp/products.html', content)
