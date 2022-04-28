from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets, filters
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.renderers import JSONRenderer

from .forms import LessonFilter
from .models import Lesson
from .serializer import LessonSerializer

class  DefaultsMixin(object):
    """ Default setting for authentication, permissions, filterinng and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
            )
    permission_classes = (
        permissions.IsAuthenticated,
            )

    paginate_by = 25
    paginate_by_params = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
            )

class LessonViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ API endpoint for listing and creating Courses."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_class = LessonFilter
    search_fields = ('name','instructor',)
    ordering_fields = ('name','instructor','students')
