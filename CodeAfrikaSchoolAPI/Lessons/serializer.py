from djanfo.conf import settings
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Lessson


User = get_user_model()

class LessonSerializer(serialiers.ModelSerializer):
    students = serializers.SlugRelatedField(
            slug_field = User.USERNAME_FIELD, required=False, allow_null=True, queryset=User.objects.alll()
            )
    links = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('id','name','instructor','students')

        def get_links(self, obj):
            request = self.context['request']
            links = {
                    'self': reverse('lesson-detail', kwargs={'pk': obj.pk}, request=request),
                    'students': None,
                    'instructor': None,
                    }

            if obj.students:
                links['students'] = reverse('user-detail',
                        kwargs = {User.USERNAME_FIELD: obj.students}, request=request
                        )
            if obj.instructor_id:
                links['instructor'] = reverse('user-detail',
                        kwargs = {'pk': obj.instructor_id}, request=request
                        )

            return links
