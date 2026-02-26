from django.urls import path
from . import views

urlpatterns = [
    # *: Here is blog app URL patterns here
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/create/', views.CreatePostView.as_view(), name='create-post'),
    path('posts/<int:post_id>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/create/', views.CreateCommentView.as_view(), name='create-comment'),
]
