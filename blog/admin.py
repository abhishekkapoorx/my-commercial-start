from django.contrib import admin
from .models import BlogPost, BlogPostAdmin

# Register your models here.
admin.site.register(
    BlogPost,
    BlogPostAdmin
)