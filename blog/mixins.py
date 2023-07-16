from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Comment
from .serializers import CommentSerializer


class Blogmixins:
    @action(detail=True, methods=['get'])
    def categorized(self, request, slug=None):
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

    @action(detail=True, methods=['get'])
    def comments(self, request, slug=None):
        try:
            comment_data = Comment.objects.filter(post=slug)
            return Response({
                'status': True,
                'count': comment_data.count(),
                'comments': CommentSerializer(comment_data, many=True).data
            })
        except Exception as e:
            return Response({
                'status': True,
                "error": str(e),
            })

    @action(detail=True, methods=['get'])
    def comment_reply(self, request, slug=None):
        try:
            reply_data = Comment.objects.filter(replied=slug)
            return Response({
                'status': True,
                'count': reply_data.count(),
                'replies': CommentSerializer(reply_data, many=True).data
            })
        except Exception as e:
            return Response({
                'status': True,
                "error": str(e),
            })
