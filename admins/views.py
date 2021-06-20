from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm,ProductCategoryAdminForm
from products.models import ProductCategory

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
      'users': User.objects.all(),
      'title': 'GeekShop - Админ | Пользователи',
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
      'title': 'GeekShop - Админ | Регистрация',
      'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == "POST":
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
      'title': 'GeekShop - Админ | Обновление пользователя',
      'form': form,
      'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
      'categories': ProductCategory.objects.all(),
      'title': 'GeekShop - Админ | Категории',
    }
    return render(request, 'admins/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = ProductCategoryAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductCategoryAdminForm()
    context = {
      'title': 'GeekShop - Админ | Создание категории',
      'form': form,
    }
    return render(request, 'admins/admin-categories-create.html', context)


def admin_categories_update(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    if request.method == "POST":
        form = ProductCategoryAdminForm(data=request.POST, instance=selected_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = ProductCategoryAdminForm(instance=selected_category)
    context = {
      'title': 'GeekShop - Админ | Обновление пользователя',
      'form': form,
      'selected_category': selected_category,
    }
    return render(request, 'admins/admin-categories-update-delete.html', context)


def admin_categories_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categories'))