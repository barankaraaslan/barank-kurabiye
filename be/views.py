from django.contrib.auth.models import User

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.decorators import api_view

@api_view()
def images(request, pk):
	if request.method == 'GET':
		user = User.objects.get(id=pk)
		images = BirthdayImage.objects.filter(user=user).order_by('id')
		paginator = LimitOffsetPagination()
		page = paginator.paginate_queryset(images, request)
		serializer = BirthdayImageSerializer(page, many=True, context={'request': request})		
		
		return paginator.get_paginated_response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

	@action(detail=True, methods=['get'])
	def images(self, request, pk=None):
		user = self.get_object()
		images = BirthdayImage.objects.filter(user=user).order_by('id')
		paginator = PageNumberPagination()
		paginator.page_size = 1
		page = paginator.paginate_queryset(images, request)
		serializer = BirthdayImageSerializer(page, many=True, context={'request': request})
		return paginator.get_paginated_response(serializer.data)

	@action(detail=True, methods=['get'])
	def imagesbe(self, request, pk=None):
		user = self.get_object()
		images = BirthdayImage.objects.filter(user=user).order_by('id')
		paginator = PageNumberPagination()
		paginator.page_size = 10
		page = paginator.paginate_queryset(images, request)
		serializer = BirthdayImageSerializer(page, many=True, context={'request': request})
		return paginator.get_paginated_response(serializer.data)

class BirthdayImageViewSet(viewsets.ModelViewSet):
	serializer_class = BirthdayImageSerializer
	queryset = BirthdayImage.objects.all()