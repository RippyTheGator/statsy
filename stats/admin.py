from django.contrib import admin
from .models import Player, Team


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {'fields': ['full_name', 'birth_date', 'birth_city',
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
    list_display = ('full_name', 'team', 'birth_date', 'primary_position', 'active', )
    list_filter = ('team', 'active', 'primary_position')
    search_fields = ('first_name', 'last_name', 'year_drafted')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_active', 'name', 'division', 'conference', 'official_site')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
