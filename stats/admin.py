from django.contrib import admin
from .models import Player, Team


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {'fields': ['full_name', 'first_name', 'last_name', 'birth_date', 'birth_city',
                                    'birth_country', 'nationality', 'height',
                                    'weight', ]}),
        ('Player Details', {'fields': ['active', 'rookie', 'roster_status', 'primary_number',
                                       'team', 'primary_position',
                                       'shoot_catches']}),
        ('Draft Details', {'fields': ['draft', 'year_drafted',
                                      'round_drafted', 'selection_number']}),
        ('Captain Status', {'fields': ['captain', 'alternate_captain'],
                            'classes':['collapse']})
    ]
    list_display = ('id', 'full_name', 'team', 'birth_date', 'primary_position', 'active', )
    list_filter = ('team', 'active', 'primary_position')
    search_fields = ('first_name', 'last_name', 'year_drafted', 'id', 'full_name')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_active', 'name', 'division', 'conference', 'official_site')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
