from django import template
from django.db.models import fields
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
# Create your views here.


class UsersListView(ListView):
    model = ShopUser
    fields = '__all__'
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# class UserCreateView(CreateView):
#     model = ShopUser
#     template_name = 'adminapp/user_update.html'
#     success_url = reverse_lazy('admin:users')
#     fields = ['username', 'first_name', 'password', 'email', 'avatar']


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/create_category.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/create_category.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/delete_category.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.success_url)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid:
            try:
                user_form.save()
                return HttpResponseRedirect(reverse('admin:users'))
            except:
                user_form = ShopUserRegisterForm(request.POST, request.FILES)

    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'form': user_form}
    return render(request, 'adminapp/user_update.html', content)


def user_update(request, pk):
    title = 'пользаватели/редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(
            request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'form': edit_form}
    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    title = 'пользователи/удаление'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        # user.is_active = False
        # user.save()
        user.delete()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}
    return render(request, 'adminapp/user_delete.html', content)


def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()

    content = {'title': title, 'objects': categories_list}
    return render(request, 'adminapp/categories.html', content)


def products(request, pk):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {'title': title, 'category': category, 'objects': products_list}
    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    title = 'создание продукта'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': title,
               'update_form': product_form, 'category': category}

    return render(request, 'adminapp/product_update.html', content)


def product_read(request, pk):
    title = 'о продукте'
    product = get_object_or_404(Product, pk=pk)
    content = {'title': title, 'object': product}
    return render(request, 'adminapp/product_read.html', content)


def product_update(request, pk):
    title = 'редактирование продукта'
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(
            request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    content = {'title': title, 'update_form': edit_form,
               'category': edit_product.category}
    return render(request, 'adminapp/product_update.html', content)


def product_delete(request, pk):
    title = 'продукт/удаление'
    product = get_object_or_404(Product, pk=pk)
    category = product.category
    if request.method == 'POST':
        # product.delete()
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[category.pk]))
    content = {'title': title, 'product_to_delete': product}
    return render(request, 'adminapp/product_delete.html', content)
