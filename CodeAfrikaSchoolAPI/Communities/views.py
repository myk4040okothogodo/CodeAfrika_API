from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model



from  rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer

from  .forms import CommunityFilter
from  .models import Community
from  .serializer import CommunitySerializer


User = get_user_model()


class DefaultsMixin(object):
    """ Default settings fro view authentication, permissions, filtering and pagination."""


    #authentication_classes = (
    #        authentication.BasicAuthentication,
    #        authentication.TokenAuthentication,
    #        )
    #permission_classes = (
    #        permissions.IsAuthenticated,
    #        )

    paginate_by = 25
    paginate_by_params ='page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
            )


class CommunityViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ API endpoint fro listing and creating communities."""
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    filter_class = CommunityFilter
    search_fields = ('name')
    ordering_fields = ('name','topics','members','courses','articles',)



