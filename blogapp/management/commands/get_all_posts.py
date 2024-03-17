from django.core.management import BaseCommand
from blogapp.models import Post


class Command(BaseCommand):
    help = 'Get all authors'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        for post in posts:
            self.stdout.write(f'{post.title}')