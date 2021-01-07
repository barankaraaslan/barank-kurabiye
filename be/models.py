from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BirthdayMessage(models.Model):
	user = models.OneToOneField(User, related_name='birthday_message', on_delete=models.CASCADE)	
	text = models.TextField(blank=True)
		
class ProfileImage(models.Model):
	user = models.OneToOneField(User, related_name='profile_image', on_delete=models.CASCADE)	
	data = models.TextField(blank=True)

class BirthdayImage(models.Model):
	user = models.ForeignKey(User, related_name='birthday_images', on_delete=models.CASCADE)	
	data = models.TextField(blank=True)
	title = models.CharField(max_length=255, blank=True)