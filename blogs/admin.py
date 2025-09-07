from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'is_published', 'views_count')
    list_filter = ('id', )
    search_fields = ('title', 'content')