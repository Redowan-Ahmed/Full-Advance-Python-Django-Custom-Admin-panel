from rest_framework import viewsets
from .models import Post, Category, Tag
from .serializers import PostSerializer, CategorySerializer
from rest_framework import filters
from .mixins import Blogmixins
# Create your views here.


class BlogPosts(viewsets.ModelViewSet, Blogmixins):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$title', '$description','tags__name', 'category__name']




class BlogCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$title', '$description','tags__name', 'category__name']