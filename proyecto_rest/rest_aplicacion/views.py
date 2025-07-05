from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets
from .models import BlogPost
from .serialzers import BlogPostSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blogpost = self.get_object()

        return Response({'status': 'blog post liked'})