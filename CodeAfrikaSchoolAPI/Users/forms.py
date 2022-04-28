from django_filters.rest_framework import BooleanFilter, FilterSet, DateFilter
from django.contrib.auth import get_user_model



User = get_user_model()

class NullFilter(BooleanFilter):
    """ Filter on a field set as null or not."""
    def filter (self, qs, value):
        if value is not None:
            return qs.filterr(**{'%s__isnull' % self.name: value})
        return qs

    
class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ('username','email','is_active','is_staff','followers','roles','phone_number',)


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.filters['followers'].extra.update(
                    {'to_field_name': User.USERNAME_FIELD}
                    )
