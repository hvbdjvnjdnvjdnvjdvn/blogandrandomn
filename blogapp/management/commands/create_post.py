from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from random import choice

from blogapp.models import Post, Author


class Command(BaseCommand):
    help = 'Create post'


    def add_arguments(self, parser):
        parser.add_argument('release_date')


    def handle(self, *args, **kwargs):
        release_date = kwargs['release_date']
        authors = Author.objects.all()
        title = lorem_ipsum.words(5, common=False).capitalize()
        content = lorem_ipsum.paragraphs(5, common=False)
        category = choice(lorem_ipsum.WORDS).capitalize()
        author = choice(authors)
        post = Post(
            release_date=release_date, 
            title=title,
            content=content, 
            category=category, 
            author=author,
        )
        post.save()
        
        self.stdout.write(f'{post.title}')