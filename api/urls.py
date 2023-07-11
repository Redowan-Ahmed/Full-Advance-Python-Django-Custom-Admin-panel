from django.urls import include, path
from rest_framework import routers
from .defaultviews import GroupViewSet, UserViewSet
from adminpanel import views
from aliscrape.views import get_product_data

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', views.ProductsViewset)
router.register(r'images', views.ImageGalleryView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get_data/', get_product_data ),
    #path('get_data/<str:slug>', get_products_by_ur ),
]
