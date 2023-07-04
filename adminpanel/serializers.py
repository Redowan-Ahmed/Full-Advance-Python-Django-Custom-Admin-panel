from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ShopProduct, ProductVariationsImageGallery, ProductVariation, ProductImageGallery


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ProductImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageGallery
        fields = '__all__'


class ProductVariationsImageGallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductVariationsImageGallery
        fields = '__all__'

class ProductVariationSerializer(serializers.ModelSerializer):
    variant_product_images = ProductVariationsImageGallerySerializers(many =True)
    class Meta:
        model = ProductVariation
        fields = '__all__'

class ShopProductSerializer(serializers.ModelSerializer):
    variant_products = ProductVariationSerializer(many=True)
    product_images = ProductImageGallerySerializer( many= True)
    class Meta:
        model = ShopProduct
        fields = '__all__'


