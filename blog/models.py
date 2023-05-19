from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default="")
    head0 = models.CharField(max_length=500, default="")
    cHead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    cHead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    cHead2 = models.CharField(max_length=5000, default="")
    
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/thumbnails',default="")

    def __str__(self):
        return self.title

class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "postId",
        "title",
        "head0",
        "head1",
        "head2",
        "pub_date"
    )