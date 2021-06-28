from django.urls import path

from users.views import UserLoginView, UserRegisterView, UserLogoutView, profile

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('logout/', UserLogoutView.as_view(), name = 'logout'),
]