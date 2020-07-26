import django_tables2 as tables
from django_tables2.utils import A
from .models import Player, Team


class PlayerTable(tables.Table):
    full_name = tables.LinkColumn('player_info', args=[A("id"), A("first_name"), A("last_name")])

    class Meta:
        model = Player
        #template_name = 'django_tables2/bootstrap-responsive.html'
        exclude = ('id', )
        attrs = {'class': 'paleblue'}
        order_by = "-view_count"
