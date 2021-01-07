import datetime
import base64

from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *
from .strings import *

@login_required
def index(request):
	if request.method == 'GET':
		return render(request, 'index.html', {
			'user':request.user,
			})

@login_required
def profile_image(request):
	message = ""
	if request.method == 'POST':
		for filekey in request.FILES.keys():
			data = request.FILES[filekey]

			request.user.profile_image.data = "data:" + data.content_type + ";base64," + base64.b64encode(data.read()).decode('utf-8')
			request.user.profile_image.save()

		message = add_birthday_image_succsess_message

	if not request.is_ajax():
		return render(request, 'profile_image.html', {
			'message': message,
			})
	else:
		return HttpResponse()

@login_required
def birthday_message(request):
	message = ""
	if request.method == 'GET':
		form = BirthdayMessageForm(instance=request.user.birthday_message)
	if request.method == 'POST':
		form = BirthdayMessageForm(request.POST, instance=request.user.birthday_message)
		if form.is_valid():
			form.save()
			message = birthday_message_success_message
	return render(request, 'birthday_message.html', {
		'form': form,
		'message': message
		})
	
@login_required
def add_birthday_image(request):
	message = ""
		
	if request.method == 'POST':
		for data in request.FILES.getlist('data'):
			image = BirthdayImage()
			image.data = "data:" + data.content_type + ";base64," + base64.b64encode(data.read()).decode('utf-8')
			image.user = request.user
			image.save()
		message = add_birthday_image_succsess_message

	return render(request, 'add_birthday_image.html', {
		'message': message,
		})

@login_required
def multiple_birthday_image(request):
	message = ""
		
	if request.method == 'POST':

		for filekey in request.FILES.keys():
			data = request.FILES[filekey]
			image = BirthdayImage()
			image.data = "data:" + data.content_type + ";base64," + base64.b64encode(data.read()).decode('utf-8')
			image.user = request.user
			image.save()
		message = add_birthday_image_succsess_message

	if not request.is_ajax():
		return render(request, 'multiple_birthday_image.html', {
			'message': message,
			})
	else:
		return HttpResponse()

@login_required
def delete_birthday_image(request, id):
	requested_image = BirthdayImage.objects.get(id=id)
	if not (requested_image.user == request.user):
		return render(request, 'permission_denied.html', {
			'message': 'Bu sayfaya erisiminiz yok'
			})

	requested_image.delete()
	if not request.is_ajax():
		if request.method == 'GET':
			return redirect(index)
	else:
		return HttpResponse()

@login_required
def birthday_image(request, id):
	image = BirthdayImage.objects.get(id=id)
	if not (image.user == request.user):
		return render(request, 'permission_denied.html', {
			'message': 'Bu sayfaya erisiminiz yok'
			})
	return render(request, 'birthday_image.html', {
		'image': image
		})

@login_required
def profile(request):
	if request.method == 'GET':
		form = UserForm(instance=request.user)
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	return render(request, 'profile.html', {
		'form' : form
		})

def signup(request):
	if request.method == 'GET':
		userForm = UserCreationForm()
		return render(request, 'signup.html', {'form' : userForm})
	if request.method == 'POST':
		userForm = UserCreationForm(request.POST)
		try:
			user = userForm.save()
			BirthdayMessage.objects.create(user=user)
			ProfileImage.objects.create(user=user)
		except ValueError as e:
			return render(request, 'signup.html', {'form' : userForm})
		return redirect(index)