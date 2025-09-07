from django.urls import path

from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('blogs/list/', views.BlogListView.as_view(), name='blogs_list'),
    path('blogs/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blogs/detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete'),
]

