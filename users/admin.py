from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', )
    list_filter = ('first_name', 'last_name', 'email', 'country', )
    search_fields = ('first_name', 'last_name', 'username', 'country', 'email', 'phone_number', )