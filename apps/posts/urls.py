from django.urls import path
from .views import PostListView, PostDetailView
from .import views
from .views import posts

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts_individual'),
]
