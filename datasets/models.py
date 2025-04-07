from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Dataset(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    file = models.FileField(upload_to='datasets/')
    file_size = models.PositiveIntegerField(help_text="Size in KB", blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True)
    categories = models.ManyToManyField(Category, related_name='datasets')
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='datasets')
    source_url = models.URLField(blank=True)
    license = models.CharField(max_length=100, blank=True)
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
