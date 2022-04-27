from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Community


User = get_user_model()


class CommunitySerializer(models.Model):
    """A serializer a for community model data."""
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = Community
        fields = ['id','name','members','topics','community_champion','projects','courses','articles']

    def get_links(self, obj):
        request = self.context['request']

        return {
               'self': reverse('community-detail',
                   kwargs = {'pk': obj.pk}, request=request),
               'members': reverse('user-list', request=request) + '?community={}'.format(obj.pk),

               'topics' : reverse('topic-list',request=request) + '?community={}'.format(obj.pk),

               'community_champion' : reverse('champions', request=request ) + '?community={}'.format(obj.pk),

               'projects': reverse('project-list', request=request)+ '?community={}'.format(obj.pk),

               'courses' : reverse('course-list', request=request) + '?community={}'.format(obj.pk),

               'articles': reverse('article-list', request=request) + '?community={}'.format(obj.pk),
            

            }


