from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ShopProduct, MediaGallery
from .serializers import ShopProductSerializer, MediaGallerySerializer, OpProductSerializer
from .mixxins import BlogMixxing

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

def index(request):
    return HttpResponseRedirect('/api/')


class ProductsViewset(viewsets.ModelViewSet, BlogMixxing):
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    queryset = (
        ShopProduct.objects.select_related('author').prefetch_related(
            'variant_products', 'variant_products__variant_product_images', 'product_images')

    )
    serializer_class = ShopProductSerializer



class MediaGalleryView(viewsets.ModelViewSet):
    queryset = MediaGallery.objects.all()

    serializer_class = MediaGallerySerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
