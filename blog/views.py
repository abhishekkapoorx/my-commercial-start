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

def blogPost(request, id):
    post = BlogPost.objects.filter(postId = id)[0]
    return render(request, "blog/blogpost.html", {"post":post})
