from django.urls import path
from .views import user_log, login_view, profile_view, explore_profile, read_profile, profile_update, email_send, view_email

urlpatterns =[
    path('signup/', user_log, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('explore/',explore_profile, name='exlore' ),
    path('explore/profile/<int:id>', read_profile),
    path('profile_update/<int:id>', profile_update, name='profile_update'),
    path('mail/',email_send, name='email'),
    path('create_email/', view_email)
]