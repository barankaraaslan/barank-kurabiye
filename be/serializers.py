from django.contrib.auth.models import User

from rest_framework import serializers

from .models import *

class ProfileImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProfileImage
		fields = ['data']
		
class BirthdayMessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = BirthdayMessage
		fields = ['text']

class BirthdayImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = BirthdayImage
		fields = ['id', 'data']

class UserSerializer(serializers.ModelSerializer):
	profile_image = ProfileImageSerializer()
	birthday_message = BirthdayMessageSerializer()
	class Meta:
		model = User
		fields = [
		'id',
		'first_name', 
		'last_name', 
		'birthday_message', 
		'profile_image', 
		]
