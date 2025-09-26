from django.urls import path

from .forms import CustomAuthenticationForm
from .views import RegisterView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]