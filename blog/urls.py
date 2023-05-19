from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/", views.blogPost, name="BlogPost")
]
