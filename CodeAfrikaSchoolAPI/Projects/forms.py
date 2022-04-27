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

    
class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = ('name','language','modules',)


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.filters['modules'].extra.update(
                    {'to_module_name': Module.name}
                    )
