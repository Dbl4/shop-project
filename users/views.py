from django.shortcuts import HttpResponseRedirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, ShopUserProfileEditForm
from baskets.models import Basket
from users.models import User, ShopUserProfile

from geekshop import settings


def send_verify_email(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])

    title = f'Активация на сайте, пользователя - {user.username}'
    message = f'Для активации вашей учетной {user.email} записи, на портале {settings.DOMAIN_NAME}' \
              f' перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email],fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            #auth.login(request, user) в лекции передается такой параметр, но у меня естественно выдает ошибку что нужно прописать мне я не понял
            #UserLoginView(user) - не работает
            return render(request, 'users/verification.html')
        else:
            print(f'error activation user {user.username}')
            return render(request, 'users/verification.html')
    except Exception as err:
        print(f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse('index'))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Авторизация'
        return context


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Регистрация'
        return context

    def form_valid(self, form):
        super().form_valid(form)
        user = form.save()
        if send_verify_email(user):
            print('Сообщение отправлено.')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print('Не удалось отправить сообщение.')
            return HttpResponseRedirect(reverse('users:login'))


class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_message = 'Изменения сохранены!'

    def get_success_url(self):
        return reverse_lazy('users:profile', args =(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Профиль'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

# class UserProfileUpdateEditView(SuccessMessageMixin, UpdateView):
#
#     """
#     не понял как прикрутить в моем случае эту форму. Получается у меня в в профиле будут 3 модели (User,
#     Basket и UserProfileUpdateEditView), так как у меня проект немного отличается, я не знаю
#     как это сделать в моем случае? Насколько я понимаю,
#     через один класс (в моем случае изначально UserProfileUpdateView) нельзя использовать 2 формы
#     одновременно.Создал отдельную модель ShopUserProfile и форма ShopUserProfileEditForm, все закинул в данный класс
#     Если смотреть в админке все работает и создается, но на странице не отображается. Возможно что-то нужно прописать в
#     profile_html для отображения. Помогите пожалуйста..
#     """
#
#     model = ShopUserProfile
#     template_name = 'users/profile.html'
#     form_class = ShopUserProfileEditForm
#     success_message = 'Изменения сохранены!'
#
#     def get_success_url(self):
#         return reverse_lazy('users:profile', args =(self.object.id,))
#
#     def get_context_data(self, **kwargs):
#         context = super(UserProfileUpdateEditView, self).get_context_data(**kwargs)
#         return context


class UserLogoutView(LogoutView):
    template_name = 'users/login.html'
