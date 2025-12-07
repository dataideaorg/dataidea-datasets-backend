from django.contrib import admin
from .models import Dataset, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'file_type', 'created_at', 'download_count')
    list_filter = ('categories', 'file_type', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'tags', 'file')
    readonly_fields = ('download_count', 'created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'author')
        }),
        ('External File Link', {
            'fields': ('file', 'file_type', 'file_size', 'license'),
            'description': 'Provide the external URL to the dataset file (Kaggle, GitHub, Google Drive, etc.)'
        }),
        ('Categorization & Source', {
            'fields': ('categories', 'tags', 'source_url')
        }),
        ('Statistics', {
            'fields': ('download_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
