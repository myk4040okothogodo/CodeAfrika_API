from django.db import models
from django.conf import settings
from  django.utils.translation import ugettext_lazy as_

class Post(models.Model):

    QUESTION_POST = 1
    GENERAL_POST  = 2
    POST_TYPE = (
        (QUESTION_POST, _('question_post')),
        (GENERAL_POST, _('general_post'))
            )
    """ A single post made by a member"""
    creator = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="post_creator", null=False, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    post_type = models.PositiveSmallIntegerField(choices=POST_TYPE, primary_key=True)
    favorited_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="userswho_like")
