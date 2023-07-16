from rest_framework import viewsets
from .models import Post, Category, Tag
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CategorySerializer
from rest_framework import filters
from .mixins import Blogmixins
# Create your views here.


class BlogPosts(viewsets.ModelViewSet, Blogmixins):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$title', '$description','tags__name', 'category__name']
    ordering_fields = ['title', 'created_at','updated_at', 'thumbnail','category','tags']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class BlogCategory(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$title', '$description','tags__name', 'category__name']
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
