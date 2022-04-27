from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse

from .model import Post

User = get_user_model()


class PostSErializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    favorited_by = serializers.SlugRelatedField(
       slug_field = User.USERNAME_FIELD, required=False, allow_null=True,
       queryset= User.objects.all())
    
    class Meta:
        model = Post
        fields = ('id', 'creator','content','post_type','favorited_by','links')


    def get_links(self, obj):
        request = elf.context['request']
        links = {
                'self': reverse('post-detail', kwargs={'pk': obj.pk}, request=request),
                 'creator': None,
                 'favorited_by': None

                }
        if obj.creator_id:
            links['creator'] = reverse('user-detail',
                kwargs = {'pk': obj.creator_id}, request=request
                    )
        if obj.favorited_by:
            links['favorited_by'] = reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: obj.favorited_by}, request=request
                    )
        return links

