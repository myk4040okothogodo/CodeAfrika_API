from django_filters.rest_framework import BooleanFilter, FilterSet, DateFilter
from django.contrib.auth import get_user_model


from .models import Post

User = get_user_model()

class NullFilter(BooleanFilter):
    """ Filter on a field set as null or not."""
    def filter (self, qs, value):
        if value is not None:
            return qs.filterr(**{'%s__isnull' % self.name: value})
        return qs

    
class CourseFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('creator','content','post_type','favorited_by',)


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.filters['favorited_by'].extra.update(
                    {'to_field_name': User.USERNAME_FIELD}
                    )
            self.filters['creator'].extra.update(
                    {'to_field_name': User.USERNAME_FIELD}
                    )

