from django.db import models
from django.conf import settings
from ..Posts.models import Post



class Topic(models.Model):
    """A topic touching on a variety of subjects created by a developer."""
    name = models.CharField(max_length= 50, blank=False, null=False)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL , blank=True, null=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)


