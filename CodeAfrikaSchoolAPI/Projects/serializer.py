from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse


from .model import Project



class ProjectSerializer(serializers.ModelSerializer):
    links = serializers.SeriazlizerMethodField()

    class Meta:
        model = Project
        fields = ('id','name','language','modules','links')


    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('project-detail',
                kwargs = {'pk': obj.pk}, request=request),
            'modules': none,

                }

        if obj.modules:
            links['modules'] = reverse('module-detail',
                kwargs = {'pk': obj.modules}, request=request
                    )
        return links
