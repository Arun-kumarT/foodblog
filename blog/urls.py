
# blog/urls.py
from django.urls import path
from .views import PostListCreateView, PostDetailView, CategoryListCreateView
from django.urls import path
from .views import post_list
urlpatterns = [
    path('', post_list, name='post-list'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Delete happens here
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]



