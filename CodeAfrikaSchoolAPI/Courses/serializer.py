from django.conf import settings
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Course
from  django.contrib.auth import get_user_model


User = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    candidates = serializers.SlugRelatedField(
            slug_field = User.USERNAME_FIELD, required=False, allow_null=True, queryset=User.objects.all()
            )
    links = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id','name','practical_assesment','lessons','course_category','difficulty_level', 'candidates', 'links')


        def get_links(self, obj):
            request = self.context['request']
            links = {
                'self': reverse('course-detail', kwargs={'pk': obj.pk}, request=request),
                'candidates' : None,
                'lessons':  None,
                    }

            if obj.lessons:
                links['lessons'] = reverse('lesson-detail',
                        kwargs = {'pk' : obj.lessons}, request= request
                        )
            if obj.candidates:
                links['candidates'] = reverse('user-detail',
                        kwargs = {User.USERNAME_FIELD: obj.candidates}, request=request
                        )
            return links



