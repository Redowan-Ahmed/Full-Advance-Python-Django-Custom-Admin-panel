from django.urls import include, path
from rest_framework import routers
from .defaultviews import GroupViewSet, UserViewSet
from adminpanel import views
from blog.views import BlogPosts, BlogCategory
from aliscrape.views import get_product_data

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', views.ProductsViewset)
router.register(r'media-files', views.MediaGalleryView, basename='media')
router.register(r'blogs', BlogPosts, basename='post')
router.register(r'blog-categories', BlogCategory, basename='blog-category')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get_data/', get_product_data ),
    #path('get_data/<str:slug>', get_products_by_ur ),
]
