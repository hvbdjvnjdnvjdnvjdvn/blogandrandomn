from random import choice, randint, uniform
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from myapp2.models import Category, Product


class Commands(BaseCommand):
    help = 'Generate fake products.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продктов для генерации')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'продукт номер {i}',
                category=choice(categories),
                description='длинное описание продукта, которое и так никто не читает',
                price=uniform(0.01, 999_999.99) ,
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))

        Product.objects.bulk_create(products)