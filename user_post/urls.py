from django.urls import path
from .views import signup, profile_del, login, home, profile, profile_update

urlpatterns =[
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path("profile/<int:id>/", profile, name="profile"),
    path("profile/delete/<int:id>/", profile_del, name="profile_del"),
    path("profile/update/<int:id>/", profile_update, name="profile_update"),

]