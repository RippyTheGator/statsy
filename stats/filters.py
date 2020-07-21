import django_filters
from .models import Player


class PlayerFilter(django_filters.FilterSet):
    # first_name = django_filters.CharFilter(label="First Name", lookup_expr='icontains')
    # last_name = django_filters.CharFilter(
    #     field_name="last_name", lookup_expr='icontains')
    # roster_status = django_filters.

    class Meta:
        model = Player
        fields = {
            'first_name': ['icontains', ],
            'last_name': ['icontains', ],
            'roster_status': ['exact']
        }
