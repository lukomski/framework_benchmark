from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from fwbm.serializers import BlogSerializer
from fwbm.models import Blog

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    @action(detail=False, methods=['post', 'get'])
    def fill_in(self, request):
        N = request.GET.get('N', 10)
        for idx in range(int(N)):
            b = Blog(name=f'Some name {idx}', tagline='Some tagline {idx}')
            b.save()
        return Response({'Count of Blogs': Blog.objects.count()})
    
    @action(detail=False, methods=['post', 'get'])
    def clear(self, request):
        Blog.objects.all().delete()
        return Response({'Count of Blogs': Blog.objects.count()})