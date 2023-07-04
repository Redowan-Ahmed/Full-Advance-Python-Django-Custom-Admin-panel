from django.contrib import admin
from django.utils.html import format_html
from .models import ShopProduct, ProductVariationsImageGallery, ProductVariation, ProductImageGallery

# Register your models here.


class ShopProductAdmin(admin.ModelAdmin):
    # product list page  customize

    list_display = ('Thumbnail', 'product_name', 'regular_price',
                    'discounted_price', 'schedule_discount', 'created_at', 'updated_at')
    # By this  you can show or hide django admin panel list display objects . By this you can also define any function and mathematical terms and show in the list
    actions_on_bottom = True
    # By this True value here django admin panel will show action form at the Bottom. if the value is False the action form will be not displayed at bottom.
    list_display_links = ['Thumbnail', 'product_name']
    # By this tuple if you add multiple objects the clickable link will be add on all the listed objects
    actions_on_top = True
    # By this True value here django admin panel will show action form at the top. if the value is False the action form will be not displayed at top.
    list_per_page = 10
    # By adding any numeric value here depending on the value the admin panel will show products or objects in a page and rest of them will show in the next page and at the bottom it will show a pagination .
    list_editable = ['regular_price', 'discounted_price', 'schedule_discount']
    # this helps to change value in the object list page instead of going to edit page to make small changes, Also by this method you can also edit multiple object single data and save. But The value of 'product_name' cannot be in both 'list_editable' and 'list_display_links'.
    list_filter = ['regular_price',
                   'discounted_price', 'created_at', 'updated_at']

    search_fields = ['product_name']

    # product Edit page Customize

    fields = ['product_name', 'short_description', 'description', 'sku', 'regular_price',
              'discounted_price', 'schedule_discount', 'author', 'thumbnail', 'thumbnail_preview']
    # this helps to add a custom serial way form show and remove or add any extra fields in the editing page
    exclude = ['']
    # this helps to exclude or remove any field from the editing page.

    save_on_top = True
    # this helps to show or remove save button section with functionality at top

    save_as_continue = True
    # this helps to show or remove save and continue editing button with functionality

    save_as = True
    # this helps to add a button with functionality to save the item as new instead of update the existing item in edit page.

    readonly_fields = ('thumbnail_preview',)
    # this helps to define any files as readonly, which is not editable

    def Thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumbnail.url}" width="50px" height="50px" />')
    # to show the thumbnail image in the list

    def thumbnail_preview(self, obj):
        return format_html(f'<img width="120px" src="{obj.thumbnail.url}" >')
    # to show Preview the thumbnail image in the edit page


admin.site.register(ShopProduct, ShopProductAdmin)


class ProductVariationImageGalaryAdmin(admin.ModelAdmin):
    list_display = ('Thumbnail', 'variant_product', 'variant_product_details', 'created_at','updated_at')

    list_display_links = ['Thumbnail', 'variant_product']
    
    list_filter = ['created_at', 'updated_at']
    
    fields = ('variant_product', 'image', 'thumbnail_preview')
    
    readonly_fields = ('thumbnail_preview',)
    
    def Thumbnail(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="50px" height="50px" alt="{obj.variant_product.variation_name}" />')
    # to show the thumbnail image in the list

    def thumbnail_preview(self, obj):
        return format_html(f'<img width="120px" src="{obj.image.url}" >')
    # to show Preview the thumbnail image in the edit page

    def variant_product_details(self, obj):
        return f'Type: {obj.variant_product.variation_type} = {obj.variant_product.variation_name}'


admin.site.register(ProductVariationsImageGallery, ProductVariationImageGalaryAdmin)

class ProductVariationAdmin(admin.ModelAdmin):
    # product list page  customize

    list_display = ('Thumbnail','product' ,'variation_type', 'variation_name', 'regular_price',
                    'discounted_price', 'schedule_discount', 'created_at', 'updated_at')
    # By this  you can show or hide django admin panel list display objects . By this you can also define any function and mathematical terms and show in the list
    actions_on_bottom = True
    # By this True value here django admin panel will show action form at the Bottom. if the value is False the action form will be not displayed at bottom.
    list_display_links = ['Thumbnail', 'product']
    # By this tuple if you add multiple objects the clickable link will be add on all the listed objects
    actions_on_top = True
    # By this True value here django admin panel will show action form at the top. if the value is False the action form will be not displayed at top.
    list_per_page = 10
    # By adding any numeric value here depending on the value the admin panel will show products or objects in a page and rest of them will show in the next page and at the bottom it will show a pagination .
    list_editable = ['regular_price', 'discounted_price', 'schedule_discount', 'variation_type', 'variation_name']
    # this helps to change value in the object list page instead of going to edit page to make small changes, Also by this method you can also edit multiple object single data and save. But The value of 'product_name' cannot be in both 'list_editable' and 'list_display_links'.
    list_filter = ['regular_price',
                   'discounted_price', 'created_at', 'updated_at', 'variation_name', 'variation_type']

    search_fields = ['variation_name', 'variation_type']

    # product Edit page Customize

    fields = ['product', 'variation_type','variation_name', 'short_description','sku','regular_price', 'discounted_price', 'schedule_discount','thumbnail_preview']
    # this helps to add a custom serial way form show and remove or add any extra fields in the editing page
    exclude = ['']
    # this helps to exclude or remove any field from the editing page.F

    save_on_top = True
    # this helps to show or remove save button section with functionality at top

    save_as_continue = True
    # this helps to show or remove save and continue editing button with functionality

    save_as = True
    # this helps to add a button with functionality to save the item as new instead of update the existing item in edit page.

    readonly_fields = ('thumbnail_preview',)
    # this helps to define any files as readonly, which is not editable

    def Thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumbnail.url}" width="50px" height="50px" />')
    # to show the thumbnail image in the list

    def thumbnail_preview(self, obj):
        return format_html(f'<img width="120px" src="{obj.thumbnail.url}" >')
    # to show Preview the thumbnail image in the edit page


admin.site.register(ProductVariation, ProductVariationAdmin)

class ProductImageGalaryAdmin(admin.ModelAdmin):
    list_display = ('Thumbnail', 'product', 'created_at','updated_at')

    list_display_links = ['Thumbnail', 'product']
    
    list_filter = ['created_at', 'updated_at']
    
    fields = ('product', 'image', 'thumbnail_preview')
    
    readonly_fields = ('thumbnail_preview',)
    
    def Thumbnail(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="50px" height="50px" alt="{obj.product.product_name}" />')
    # to show the thumbnail image in the list

    def thumbnail_preview(self, obj):
        return format_html(f'<img width="120px" src="{obj.image.url}" >')
    # to show Preview the thumbnail image in the edit page
    
admin.site.register(ProductImageGallery, ProductImageGalaryAdmin)
