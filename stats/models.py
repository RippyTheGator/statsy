from django.db import models
import environ


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    primary_number = models.CharField(max_length=3)
    birth_date = models.DateField(auto_now=False, blank=True, null=True)
    birth_city = models.CharField(max_length=50, default='N/A')
    birth_country = models.CharField(max_length=50, default='N/A')
    nationality = models.CharField(max_length=50, default='N/A')
    height = models.CharField(max_length=10, default='N/A')
    weight = models.CharField(max_length=5, default='N/A')
    active = models.BooleanField(default=False)
    alternate_captain = models.BooleanField(default=False)
    captain = models.BooleanField(default=False)
    rookie = models.BooleanField(default=False)
    shoot_catches = models.CharField(max_length=3, default='N/A')
    roster_status = models.CharField(default='N', max_length=1)
    draft = models.ForeignKey(
        'Team', on_delete=models.SET_DEFAULT, related_name='draft', default=0)
    year_drafted = models.IntegerField(blank=True, null=True)
    round_drafted = models.IntegerField(blank=True, null=True)
    selection_number = models.IntegerField(blank=True, null=True)
    team = models.ForeignKey(
        'Team', default=0, on_delete=models.SET_DEFAULT, related_name='team')
    primary_position = models.CharField(max_length=50, default='N/A')
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    venue_name = models.CharField(max_length=50)
    abbrevation = models.CharField(max_length=3)
    first_year_of_play = models.CharField(max_length=4)
    division = models.CharField(max_length=50)
    conference = models.CharField(max_length=50)
    official_site = models.CharField(max_length=50)
    team_active = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
