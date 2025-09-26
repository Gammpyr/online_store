from django.conf import settings
from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user)
        return super().form_valid(form)

    def send_welcome_email(self, user):
        subject = 'Добро пожаловать в наш магазин!'
        message = f'{user.display_name.title()}, спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
