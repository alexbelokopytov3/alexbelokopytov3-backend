from django.urls import path, re_path
from .views import Authentication, Logout, Edit, User_delete, User_delete_form, Profile_view



urlpatterns = [
    re_path(r'authentication/$', Authentication, name = 'Authentication'),
    re_path(r'Logout/$', Logout, name = 'Logout'),
    re_path(r'^edit/$', Edit, name='Edit'),
    path('profile_delete/<int:id>/', User_delete, name='user_delete'),
    path('profile_delete_form/<int:id>/', User_delete_form, name='user_delete_form'),
    path('profile/<int:id>/', Profile_view, name='profile_view'),
]