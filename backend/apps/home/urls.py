from django.urls import path, re_path

from .views import Post_detail, Post_edit, Post_create, Comment_delete, Post_delete



urlpatterns = [
    path('<int:id>/', Post_detail, name='post_detail'),
    path('<int:id>/edit/', Post_edit, name='post_edit'),
    re_path(r'^create/$', Post_create, name='post_create'),
    path('comment_delete/<int:id>/', Comment_delete, name='comment_delete'),
    path('post_delete/<int:id>/', Post_delete, name='post_delete'),
]