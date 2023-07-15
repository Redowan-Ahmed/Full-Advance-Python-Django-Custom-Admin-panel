from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ShopProduct, MediaGallery
from .serializers import ShopProductSerializer, MediaGallerySerializer, OpProductSerializer





class BlogMixxing:

    @action(detail=False, methods=['get', 'post'])
    def OnlyProudcts(self, request, *args, **kwargs):
        products = self.queryset
        if request.method == "GET":
            serializer = OpProductSerializer(products, many=True)
            return Response({
                'data': serializer.data,
            })
        elif request.method == "POST":
            pass
        return Response({
            'data': "",
        })