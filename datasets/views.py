from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F
from .models import Dataset, Category
from .serializers import DatasetSerializer, CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'tags']
    ordering_fields = ['created_at', 'updated_at', 'download_count', 'title']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(detail=True, methods=['get'])
    def download(self, request, slug=None):
        dataset = self.get_object()
        dataset.download_count = F('download_count') + 1
        dataset.save(update_fields=['download_count'])
        dataset.refresh_from_db()
        return Response({'status': 'download count incremented',
                         'download_count': dataset.download_count})
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_datasets = Dataset.objects.order_by('-download_count')[:5]
        serializer = self.get_serializer(featured_datasets, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_datasets = Dataset.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_datasets, many=True)
        return Response(serializer.data)
