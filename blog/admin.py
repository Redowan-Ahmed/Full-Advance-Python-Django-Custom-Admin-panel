from django.contrib import admin
from .models import Category, Post, Tag, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)