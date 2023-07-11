from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ShopProduct, ProductVariationsImageGallery, ProductVariation, ProductImageGallery
from .serializers import ShopProductSerializer, ProductVariationsImageGallerySerializers, ProductImageGallerySerializer, ProductVariationSerializer

from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

def index(request):
    return HttpResponseRedirect('/api/')

class ProductsViewset(viewsets.ModelViewSet):
    queryset = ShopProduct.objects.all().order_by('-created_at')
    serializer_class = ShopProductSerializer
    #parser_classes = (MultiPartParser, FormParser)
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]