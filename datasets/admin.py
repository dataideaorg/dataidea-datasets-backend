from django.contrib import admin
from .models import Dataset, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'download_count')
    list_filter = ('categories', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'tags')
    readonly_fields = ('download_count', 'created_at', 'updated_at')
