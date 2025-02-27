from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'calc'

urlpatterns = [
    path('', views.login_view, name='login'),  # Default to login page
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('posts/', views.post_list, name='post_list'),
    path('blog/<int:id>/', views.post_detail, name='post_detail'),
    path('blog/new/', views.post_new, name='new-post'),
    path('blog/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('blog/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('logout/',views.logout_view, name='logout'),  # Logout functionality
]
