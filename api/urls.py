from django.urls import include, path
from rest_framework import routers
from .defaultviews import GroupViewSet, UserViewSet
from adminpanel import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', views.ProductsViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]