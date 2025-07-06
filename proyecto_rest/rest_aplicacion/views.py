from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BlogPost
from .serialzers import BlogPostSerializer

from rest_framework import viewsets


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blogpost = self.get_object()

        return Response({'status': 'blog post liked'})