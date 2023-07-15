from django.contrib import admin
from .models import Category, Post, Tag
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)