from django.shortcuts import render, get_object_or_404

from .models import Post, Author
from .forms import PostForm

def get_posts_by_author(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    posts = Post.objects.filter(author=author)
    return render(request, "blogapp/author_posts.html", {"posts": posts, "author": author})


def get_posts_by_id(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.views += 1
    post.save()
    content = eval(post.content)
    return render(request, "blogapp/post.html", {"post": post, "content": content})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            test = form.save()
            print(test)
            # return get_posts_by_id
    else:
        form = PostForm()
    return render(request, 'blogapp/add_post.html', {'form': form})
