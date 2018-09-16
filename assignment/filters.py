from .models import Assignment
import django_filters

class AssignmentFilter(django_filters.FilterSet):
    class Meta:
        model = Assignment
        fields = {'title':['icontains', ],
                  'user':['exact',],
                  'category':['icontains', ],
                  'created': ['day', 'day__gt', 'day__lt', ],
                  }