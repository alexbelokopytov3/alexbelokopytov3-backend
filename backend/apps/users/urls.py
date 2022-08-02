from django.urls import path, re_path
from .views import Authentication, Logout, Edit



urlpatterns = [
    re_path(r'authentication/$', Authentication, name = 'Authentication'),
    re_path(r'Logout/$', Logout, name = 'Logout'),
    re_path(r'^edit/$', Edit, name='Edit'),
]