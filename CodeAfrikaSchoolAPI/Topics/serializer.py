from django.conf import settings
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Topic
from django.contrib.auth import get_user_model


User = get_user_model()


class TopicSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ('id','name','posts','created_by', 'links')


        def get_links(self, obj):
            request = self.context['request']
            links = {
                'self': reverse('topic-detail', kwargs={'pk': obj.pk}, request=request),
                'created_by' : None,
                'posts':  None,
                    }

            if obj.posts:
                links['posts'] = reverse('post-detail',
                        kwargs = {'pk' : obj.posts}, request= request
                        )
            if obj.candidates:
                links['created_by'] = reverse('user-detail',
                        kwargs = {'pk': obj.created_by_id}, request=request
                        )
            return links
