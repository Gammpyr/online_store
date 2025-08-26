from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from product_fixture'))


        # group, _ = Category.objects.get_or_create(name='Машины', description='Различные типы и марки автомобилей')
        #
        # products = [
        #     {'name': 'BMW', 'description': 'Седан', 'price': 100000, 'category': group},
        #     {'name': 'Lamborghini', 'description': 'Спорткар', 'price': 500000, 'category': group},
        #     {'name': 'Lada', 'description': 'Отечественный продукт', 'price': 60000, 'category': group},
        # ]
        #
        # for product_data in products:
        #     product, created = Product.objects.get_or_create(**product_data)
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name} {product.description}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Product already exists: {product.name} {product.description}'))