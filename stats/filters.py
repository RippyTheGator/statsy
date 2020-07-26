import django_filters
from .models import Player, Team

CHOICES = (
    ('Center', 'C'),
    ('Left Wing', 'LW'),
    ('Right Wing', 'RW'),
    ('Defenseman', 'D'),
    ('Goalie', 'G'),
)


class PlayerFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(label="First Name:", lookup_expr="icontains")
    last_name = django_filters.CharFilter(label="Last Name:", lookup_expr="icontains")
    birth_city = django_filters.CharFilter(label="Birth City", lookup_expr="iexact")
    birth_country = django_filters.CharFilter(label="Birth Country", lookup_expr="iexact")
    nationality = django_filters.CharFilter(label="Nationality", lookup_expr="iexact")
    roster_status = django_filters.CharFilter(label="Roster Status", lookup_expr="exact")
    active = django_filters.BooleanFilter(label="Is Active?", lookup_expr="exact")
    rookie = django_filters.BooleanFilter(label="Rookie", lookup_expr="exact")
    captain = django_filters.BooleanFilter(label="Captain", lookup_expr="exact")
    alternate_captain = django_filters.BooleanFilter(label="Alt. Captain", lookup_expr="exact")
    primary_number = django_filters.NumberFilter(label="Number", lookup_expr="exact")
    team = django_filters.ModelChoiceFilter(queryset=Team.objects.all(), label="Team")
    primary_position = django_filters.ChoiceFilter(
        choices=CHOICES, label="Position")
    shoot_catches = django_filters.ChoiceFilter(
        label="Shoot/Catches", choices=(('L', 'L'), ('R', 'R')))
    year_drafted = django_filters.NumberFilter(label="Year Drafted", lookup_expr="exact")
    round_drafted = django_filters.NumberFilter(label="Round Drafted", lookup_expr="exact")
    selection_number = django_filters.NumberFilter(label="Selection Number", lookup_expr="exact")
    # class Meta:
    #     model = Player
    #     fields = {
    #         'first_name': ['icontains', ],
    #         'last_name': ['icontains', ],
    #         'roster_status': ['exact']
    #     }
