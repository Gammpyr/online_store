from config.settings import CACHE_ENABLED
from .models import Product
from django.core.cache import cache


def get_category_products(category_id=None):
    """Получается список продуктов по категории (если она указана)"""
    queryset = get_all_products()
    print('---Получен кверисет---')
    if category_id:
        queryset = queryset.filter(category_id=category_id)
        print('---Отфильтрован по категориям---')
        if CACHE_ENABLED:
            cached_products = cache.get(f'products_category_{category_id}')
            print('---Попытка получения продукта из кэша---')
            if cached_products:
                print('---Возвращен кэш с категорией---')
                return cached_products
            cache.set(f'products_category_{category_id}', queryset, 60 * 15)
            print('---Создан кэш с категорией---')
    print('---Возвращает итог---')
    return queryset


def get_all_products():
    """Получается список всех продуктов"""
    if CACHE_ENABLED:
        queryset = cache.get('products_all')
        print('---Попытка получения из кэша всех продуктов---')
        if not queryset:
            print('---В Кэше нет всех продуктов---')
            print('---Запрос в БД---')
            queryset = Product.objects.all()
            cache.set('products_all', queryset, 60 * 15)
            print('---Создан кэш всех продуктов---')
    else:
        print('---Запрос в БД---')
        queryset = Product.objects.all()

    return queryset
