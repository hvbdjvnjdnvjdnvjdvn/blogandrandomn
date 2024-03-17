from django.urls import path
from . import views


urlpatterns = [
    path(
        "posts/author/<int:author_pk>/",
        views.get_posts_by_author,
        name="get_posts_by_author",
    ),
    path("posts/post/<int:post_pk>/", views.get_posts_by_id, name="get_posts_by_id"),
    path("posts/add_post", views.add_post, name="add_post"),
]
