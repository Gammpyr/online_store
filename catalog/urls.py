from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),

    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/toggle_publish/', views.ProductTogglePublishView.as_view(), name='toggle_publish'),
]

