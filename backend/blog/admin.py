from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content', 'author__username')
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
