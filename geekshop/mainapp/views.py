from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product

# Create your views here.

# контент у меня получается общий для всего сайта. Наверное это не очень хорошо
content = {
    'product_title': 'продукты',
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
    ],
    'products': Product.objects.all()[:],
    # не придумал как сделать категорию, объединяющую все категории.
    'product_categories': [{'name': 'все'}, *ProductCategory.objects.all()[2:]],
}


def index(request):
    content = {
        'title': 'главная',
        'main_menu': [
            {'href': 'index', 'name': 'домой'},
            {'href': 'products', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'}, ],
        'products': Product.objects.all()[:2]
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', content)


def products(request, pk=None):

    selected_category = ProductCategory.objects.filter(id=pk)
    categories = ProductCategory.objects.all()
    products = [Product.objects.filter(category=selected_category)]
    content = {
        'title': 'Продукты',
        'main_menu': [
            {'href': 'index', 'name': 'домой'},
            {'href': 'products', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'}, ],
        'product_categories': categories,
        'products': products,
        'selected_category': selected_category
    }
    if pk:
        return render(request, 'mainapp/category.html', content)
    return render(request, 'mainapp/products.html', content)
