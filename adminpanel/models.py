from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
import time


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
    thumbnail = models.ImageField(
        upload_to='product-images', blank=True, null=True)
    sku = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=350, blank=True,
                            unique=True, db_index=True)
    regular_price = models.DecimalField(max_digits=1000, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    schedule_discount = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    stock = models.IntegerField(default=10)
    out_of_stock = models.BooleanField(default=False)
    have_variant = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        unique_id = str(uuid.uuid4()).split('-')
        unique_slug = slugify(f'{self.product_name} {unique_id[0]}')
        slug = slugify(self.product_name)
        if not self.slug:
            if ShopProduct.objects.filter(slug=slug).exists():  # type: ignore
                self.slug = unique_slug
            else:
                self.slug = slug
        super(ShopProduct, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)


class ProductVariation(BaseModel):
    variation_type = models.CharField(max_length=100)
    product = models.ForeignKey(
        ShopProduct, on_delete=models.CASCADE, related_name='variant_products', blank=True, db_index=True)
    variation_name = models.CharField(max_length=250)
    short_description = models.TextField(
        max_length=1200, default='0', blank=True)
    sku = models.CharField(max_length=200, blank=True, null=True, unique=True)
    thumbnail = models.ImageField(
        upload_to='product-images', blank=True, null=True)
    regular_price = models.DecimalField(max_digits=1000, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    schedule_discount = models.DateTimeField(blank=True, null=True)
    stock = models.IntegerField(default=10)
    out_of_stock = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.product_name}'


class ProductImageGallery(BaseModel):
    product = models.ForeignKey(
        ShopProduct, on_delete=models.CASCADE, related_name='product_images', blank=True, db_index=True)
    image = models.ImageField(
        upload_to='product-image-gallery', blank=True, null=True)

    def __str__(self):
        return self.product.product_name


class ProductVariationsImageGallery(BaseModel):
    variant_product = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE, related_name='variant_product_images', blank=True, db_index=True)
    image = models.ImageField(
        upload_to='product-image-gallery', blank=True, null=True)

    def __str__(self):
        return self.variant_product.variation_name


class MediaGallery(BaseModel):
    media = models.FileField(
        upload_to=f'media-files/{time.strftime("%Y")}/{time.strftime("%m")}', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, default=1, db_index=True)

    def __str__(self):
        return self.author.username


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name='associated_user')

    def __str__(self):
        return self.user.username


class CartItem(BaseModel):
    product = models.ForeignKey(
        ShopProduct, on_delete=models.CASCADE, blank=True, null=True, related_name='product')

    product_variant = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE, blank=True, null=True, related_name='product_variant')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, related_name='cart')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cart.user.username
