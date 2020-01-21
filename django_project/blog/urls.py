from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new-post/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update-post/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete-post/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name = 'blog-about'),
]
