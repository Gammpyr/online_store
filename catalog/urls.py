from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),

    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]

