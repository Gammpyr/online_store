from config.settings import CACHE_ENABLED
from .models import Product
from django.core.cache import cache


def get_category_products(category_id=None):
    """Получается список продуктов по категории (если она указана)"""
    queryset = get_all_products()
    if category_id:
        queryset = queryset.filter(category_id=category_id)
        if CACHE_ENABLED:
            cached_products = cache.get(f'products_category_{category_id}')
            if cached_products:
                return cached_products
            cache.set(f'products_category_{category_id}', queryset, 60 * 15)
    return queryset


def get_all_products():
    """Получается список всех продуктов"""
    if CACHE_ENABLED:
        queryset = cache.get('products_all')
        if not queryset:
            queryset = Product.objects.all()
            cache.set('products_all', queryset, 60 * 15)
    else:
        queryset = Product.objects.all()

    return queryset
