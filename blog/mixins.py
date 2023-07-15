from rest_framework.response import Response
from rest_framework.decorators import action


class Blogmixins:
    @action(detail=True, methods=['get'])
    def ProductsByCategory(self, request, slug=None):
        try:
            category = self.queryset.filter(category__slug=slug)
            page = self.paginate_queryset(category)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(category, many=True)

            return Response({
                'status': True,
                'count': category.count(),
                'data': self.serializer_class(category, many=True).data,
            })
        except Exception as e:
            return Response({
                'e': e,
            })
