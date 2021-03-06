from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error/', views.error_page, name='error-page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('photo/details/<int:id>/', views.photo_details, name='photo-details'),

    path('profile/create', views.create_profile, name='create-profile'),
    path('profile/update/', views.update_profile, name='update-profile'),
    path('profile/delete/', views.delete_profile_page, name='delete-profile'),

    path('photos/add/', views.add_photo, name='add-photo'),
    path('photo/like/<int:pk>', views.update_likes, name='like pet photo'),
]
