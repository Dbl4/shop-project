from django.shortcuts import render
# from django.contrib import auth
# from django.urls import reverse
# Create your views here.

from users.models import User

def index(request):
    return render(request, 'admins/admin.html')


def admin_users(request):
    context = {
      'users': User.objects.all(),
      'title': 'GeekShop - Admin',
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_users_update(request, id):
    return render(request, 'admins/admin-users-update-delete.html')


def admin_users_delete(request, id):
    pass
    # return render(request, 'users/profile.html')
