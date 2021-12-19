from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product

# Create your views here.

main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


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


def products(request, pk=None):

    selected_category = ProductCategory.objects.filter(id=pk)
    categories = ProductCategory.objects.all()
    all_products = Product.objects.all()
    products = Product.objects.filter(category_id=pk)

    content = {
        'title': 'Продукты',
        'main_menu': main_menu,
        'product_categories': categories,
        'products': products,
        'selected_category': selected_category,
        'same_products': all_products[:3],
    }
    if pk:
        return render(request, 'mainapp/category.html', content)
    return render(request, 'mainapp/products.html', content)
