from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer

from .form import ModuleFilter
from .model import Module
from .serializers import ModuleSerializer

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
        filter.SearchFilter,
        filter.OrderingFilter,
            )

class ModuleViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ API endpoint for listing and creating Courses."""
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_class = ModuleFilter
    search_fields = ('name',)
    ordering_fields = ('name','tasks',)
