from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm,ProductCategoryAdminForm
from products.models import ProductCategory


class UserTemplateView(TemplateView):
    template_name = 'admins/admin.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserTemplateView, self).dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        return context
        
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#       'title': 'GeekShop - Админ | Регистрация',
#       'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)


class UserCreateView(CreateView):
    midel = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == "POST":
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {
#       'title': 'GeekShop - Админ | Обновление пользователя',
#       'form': form,
#       'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    
    def get_context_data(self, list_object=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = ProductCategoryAdminForm
    success_url = reverse_lazy('admins:admin_categories')

    def get_context_data(self, list_object=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Создание категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories_update(request, id):
#     selected_category = ProductCategory.objects.get(id=id)
#     if request.method == "POST":
#         form = ProductCategoryAdminForm(data=request.POST, instance=selected_category)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = ProductCategoryAdminForm(instance=selected_category)
#     context = {
#       'title': 'GeekShop - Админ | Обновление пользователя',
#       'form': form,
#       'selected_category': selected_category,
#     }
#     return render(request, 'admins/admin-categories-update-delete.html', context)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = ProductCategoryAdminForm
    success_url = reverse_lazy('admins:admin_categories')

    def get_context_data(self, list_object=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Обновление пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)



# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories_delete(request, id):
#     category = ProductCategory.objects.get(id=id)
#     category.delete()
#     return HttpResponseRedirect(reverse('admins:admin_categories'))

class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = ProductCategoryAdminForm
    success_url = reverse_lazy('admins:admin_categories')