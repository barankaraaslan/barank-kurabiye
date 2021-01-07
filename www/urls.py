from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),	
    path('accounts/profile/', views.profile, name='profile'),	
 	path('accounts/', include('django.contrib.auth.urls')),   
    path('profile_image/', views.profile_image, name='profile_image'),
    path('birthday_message/', views.birthday_message, name='birthday_message'),
    path('birthday_image/<int:id>/', views.birthday_image, name='birthday_image'),
    path('add_birthday_image/', views.add_birthday_image, name='add_birthday_image'),
    path('delete_birthday_image/<int:id>', views.delete_birthday_image, name='delete_birthday_image'),
    path('multiple_birthday_image/', views.multiple_birthday_image, name='multiple_birthday_image'),
]