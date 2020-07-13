# Generated by Django 3.0.7 on 2020-07-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0017_player_player_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='age',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_age',
        ),
        migrations.AddField(
            model_name='player',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
