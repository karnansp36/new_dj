from django.urls import path
from . import views

urlpatterns = [
    path("text/", views.text_generation, name="text_generation"),
    path("image/", views.image_generation, name="image_generation"),
]
