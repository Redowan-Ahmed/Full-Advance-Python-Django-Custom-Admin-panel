from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.html import format_html



class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class ShopProduct(BaseModel):
    product_name = models.CharField(max_length=250)
    short_description = models.TextField(
        max_length=1200, default='0', blank=True)
    description = models.TextField(max_length=5000)
    thumbnail = models.ImageField(upload_to='product-images')
    sku = models.CharField(max_length=200, blank=True, null=True, unique=True)
    regular_price = models.DecimalField(max_digits=1000, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    schedule_discount = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.product_name


class ProductVariation(BaseModel):
    variation_type = models.CharField(max_length=100)
    product = models.ForeignKey(
        ShopProduct, on_delete=models.CASCADE, related_name='product')
    variation_name = models.CharField(max_length=250)
    short_description = models.TextField(
        max_length=1200, default='0', blank=True)
    sku = models.CharField(max_length=200, blank=True, null=True,unique=True)
    thumbnail = models.ImageField(upload_to='product-images')
    regular_price = models.DecimalField(max_digits=1000, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    schedule_discount = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.product.product_name}'


class ProductImageGallery(BaseModel):
    product = models.ForeignKey(
        ShopProduct, on_delete=models.CASCADE, related_name='product_image_gallery')
    image = models.ImageField(upload_to='product-image-gallery')

    def __str__(self):
        return self.product.product_name


class ProductVariationsImageGallery(BaseModel):
    variant_product = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE, related_name='variant_product_image_gallery')
    image = models.ImageField(upload_to='product-image-gallery')

    def __str__(self):
        return self.variant_product.variation_name
