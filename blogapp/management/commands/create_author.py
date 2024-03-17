from django.core.management import BaseCommand
from django.utils import lorem_ipsum

from blogapp.models import Author


class Command(BaseCommand):
    help = 'Create author'

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('surname')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        surname = kwargs['surname']
        bio = lorem_ipsum.paragraphs(2, common=False)
        author = Author.objects.create(
            name=name, 
            surname=surname,
            email=f'{name} {surname}@mail.ru',
            bio=bio,
            birthdate='2000-12-12',
            )
        self.stdout.write(f'{author}')