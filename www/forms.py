from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from be.models import *
# Create your models here.

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']		

class BirthdayMessageForm(ModelForm):
	class Meta:
		model = BirthdayMessage
		fields = ['text']