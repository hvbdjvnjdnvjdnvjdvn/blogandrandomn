from django.core.management import BaseCommand
from blogapp.models import Post


class Command(BaseCommand):
    help = 'Get posts by author'


    def add_arguments(self, parser):
        parser.add_argument('name')


    def handle(self, *args, **kwargs):
        name = kwargs['name']
        posts = Post.objects.filter(author__fullname__icontains=name)
        for post in posts:
            self.stdout.write(f'{post.title} author: {post.author.fullname}')