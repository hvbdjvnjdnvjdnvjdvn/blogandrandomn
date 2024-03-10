from django.core.management import BaseCommand
from blogapp.models import Author


class Command(BaseCommand):
    help = 'Get all authors'

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        for author in authors:
            self.stdout.write(f'{author}')