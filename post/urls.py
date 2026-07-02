from django.urls import path
from .views import createPost, post_list

urlpatterns = [
    path("create/", createPost, name="create_post"),
    path("list/", post_list, name="post_list")
]