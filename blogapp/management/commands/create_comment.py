from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from random import choice

from blogapp.models import Comment, Post, Author


class Command(BaseCommand):
    help = 'Create comment'


    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        posts = Post.objects.all()
        content = lorem_ipsum.paragraphs(5, common=False)
        author = choice(authors)
        post = choice(posts)
        comment = Comment(
            author=author,
            post=post,
            content=content,  
        )
        comment.save()
        
        self.stdout.write(f'{comment.content}')