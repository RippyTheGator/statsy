# Generated by Django 3.0.7 on 2020-07-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0019_team_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='round_drafted',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='selection_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='year_drafted',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
