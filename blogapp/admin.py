from django.contrib import admin
from .models import Author, Post, Comment

# Register your models here.


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = [
        'name',
        'surname', 
        'email',
        'birthdate',
    ]
    list_filter = ['birthdate']
    search_fields = ['name', 'surname']
    list_editable = ['email']
    list_per_page = 100
    fieldsets = [
        ('personal info', {
            'fields': ['fulname'],
            'description': ['information about Author'],
            'classes': ['collapse']
        }),
        ('more', {
            'fields': ['name', 'surname', 'birthdate']
        }),
        ('contact', {
            'fields': ['email'],
            'classes': ['collapse']
        })
    ]


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['category', 'title', 'release_date', 'author', 'views', 'is_published']
    list_editable = ['is_published']
    search_fields = ['title', 'author']
    list_per_page = 10


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['author', 'post', 'create_date', 'change_date']
    search_fields = ['author', 'post', 'create_date', 'change_date']
    list_per_page = 10
    readonly_fields = ['change_date', 'create_date']
    fieldsets = [
        ('info', {
            'fields': ['author', 'change_date', 'create_date'],
            'classes': ['collapse'],
            })
        ]


# admin.site.register(Author)
# admin.site.register(Post)
