from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'birthday_images', BirthdayImageViewSet, basename='birthday_image')

urlpatterns = [
	path('', include(router.urls)),
	path('images/<int:pk>/', images),
]