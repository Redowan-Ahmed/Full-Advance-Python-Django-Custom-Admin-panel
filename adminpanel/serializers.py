from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ShopProduct, ProductVariationsImageGallery, ProductVariation, ProductImageGallery, MediaGallery


class MediaGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaGallery
        fields = '__all__'


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
    variant_product_images = ProductVariationsImageGallerySerializers(
        many=True)

    class Meta:
        model = ProductVariation
        fields = ['id','variation_type','variation_name','sku','regular_price','discounted_price','schedule_discount','stock','out_of_stock','short_description','product','thumbnail','variant_product_images' ]


class ShopProductSerializer(serializers.ModelSerializer):
    variant_products = ProductVariationSerializer(many=True)
    product_images = ProductImageGallerySerializer(many=True)

    class Meta:
        model = ShopProduct
        fields = ['id','slug','product_name','sku','regular_price','discounted_price','schedule_discount','stock','out_of_stock','author','thumbnail','product_images','short_description','description','have_variant','variant_products']
        

    def create(self, validated_data):
        variant_products = validated_data.pop('variant_products')
        product_images = validated_data.pop('product_images')
        product = ShopProduct.objects.create(**validated_data)

        if not variant_products == []:
            for variant_product in variant_products:

                checkvarientimages = variant_product['variant_product_images']
                print(checkvarientimages)

                product_variant = ProductVariation.objects.create(
                    product=product,
                    variation_type=variant_product['variation_type'],
                    variation_name=variant_product['variation_name'],
                    short_description=variant_product['short_description'], sku=variant_product['sku'],
                    regular_price=variant_product['regular_price'],
                    discounted_price=variant_product['discounted_price'],
                    schedule_discount=variant_product['schedule_discount'], stock=variant_product['stock'],
                    out_of_stock=variant_product['out_of_stock']
                )

                if not checkvarientimages == []:
                    for varientimg in checkvarientimages:
                        ProductVariationsImageGallery.objects.create(
                            variant_product=product_variant, **varientimg)

        if not product_images == []:
            for product_image in product_images:
                ProductImageGallery.objects.create(
                    product=product, image=product_image['image'])

        return product

class OpProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProduct
        fields = '__all__'