from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_filter = ['title']
    search_fields = ('title', 'description')
    list_per_page = 20

admin.site.register(Post, PostAdmin)

