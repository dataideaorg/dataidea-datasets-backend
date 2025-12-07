from rest_framework import serializers
from .models import Dataset, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class DatasetSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Category.objects.all(),
        source='categories'
    )

    class Meta:
        model = Dataset
        fields = [
            'id', 'title', 'slug', 'description', 'file',
            'file_size', 'file_type', 'categories', 'category_ids',
            'tags', 'author', 'source_url', 'license',
            'download_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'download_count', 'created_at', 'updated_at'] 