from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import ShopProduct, ImageGallery
from .serializers import ShopProductSerializer, ImageGallerySerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

def index(request):
    return HttpResponseRedirect('/api/')


class ProductsViewset(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = ShopProduct.objects.all().order_by('-created_at')
    serializer_class = ShopProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]


class ImageGalleryView(viewsets.ModelViewSet):
    queryset = ImageGallery.objects.all().order_by('-created_at')
    serializer_class = ImageGallerySerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]
