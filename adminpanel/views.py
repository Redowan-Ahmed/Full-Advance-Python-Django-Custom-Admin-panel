from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ShopProduct, ProductVariationsImageGallery, ProductVariation, ProductImageGallery
from .serializers import ShopProductSerializer, ProductVariationsImageGallerySerializers, ProductImageGallerySerializer, ProductVariationSerializer
# Create your views here.

def index(request):
    return HttpResponseRedirect('/api/')

class ProductViewset(viewsets.ModelViewSet):
    queryset = ShopProduct.objects.all()
    serializer_class = ShopProductSerializer