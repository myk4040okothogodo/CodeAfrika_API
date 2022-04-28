from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import authentication, permissions, viewsets
from django_filters import rest_framework as filters
from rest_framework.renderers import JSONRenderer

from .forms import CourseFilter
from .models import Course
from .serializer import CourseSerializer

class  DefaultsMixin(object):
    """ Default setting for authentication, permissions, filterinng and pagination."""

    #authentication_classes = (
    #    authentication.BasicAuthentication,
    #    authentication.TokenAuthentication,
    #        )
    #permission_classes = (
    #    permissions.IsAuthenticated,
    #        )

    paginate_by = 25
    paginate_by_params = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
            )

class CourseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ API endpoint for listing and creating Courses."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_class = CourseFilter
    search_fields = ('name')
    ordering_fields = ('name','lessons','course_category','difficulty_level','practical_assesment',)


