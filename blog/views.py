from django.shortcuts import render
from blog.models import BlogPost
# from django.http import HttpResponse

# Create your views here.
def index(request):
    blogPosts = BlogPost.objects.all()
    post = {
        "blogPost": blogPosts
    }
    return render(request, "blog/index.html", post)

def blogPost(request):
    return render(request, "blog/blogpost.html")
