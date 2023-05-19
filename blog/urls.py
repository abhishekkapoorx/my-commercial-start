from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/<int:id>", views.blogPost, name="BlogPost")
]
