from django.urls import path

from catalog import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', views.home, name='home_page'),
    path('contacts/', views.contacts, name='contacts')
]

