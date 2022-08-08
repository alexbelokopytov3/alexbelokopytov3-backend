from django.urls import path, re_path

from .views import Post_detail, Post_edit, Post_create



urlpatterns = [
    path('<int:id>/', Post_detail, name='post_detail'),
    path('<int:id>/edit/', Post_edit, name='post_edit'),
    re_path(r'^create/$', Post_create, name='post_create')
]