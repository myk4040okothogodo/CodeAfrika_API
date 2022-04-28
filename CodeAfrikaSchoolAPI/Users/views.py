from django.conf import settings
from django.core.signing import TimestampSigner
from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets
from django_filters import rest_framework as filters
from rest_framework.renderers import JSONRenderer
from rest_framework.filters import SearchFilter, OrderingFilter


from .forms import  UserFilter
from .serializer import UserSerializer


User = get_user_model()


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""
    
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,    
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )




class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing users."""
    
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD, )
    

