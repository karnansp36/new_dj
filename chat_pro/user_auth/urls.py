from django.urls import path
from . import views
from . import posts
urlpatterns =[
    path('home/', views.home),
    path('about/', views.about),
    path('signup/', views.signup),
    path('hello/', posts.hello)
]