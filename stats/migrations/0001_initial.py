# Generated by Django 3.0.7 on 2020-06-23 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('primary_number', models.IntegerField(default=0)),
                ('birth_date', models.DateField()),
                ('birth_city', models.CharField(max_length=50)),
                ('birth_country', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=5)),
                ('active', models.BooleanField(default=False)),
                ('alternate_captain', models.BooleanField(default=False)),
                ('captain', models.BooleanField(default=False)),
                ('rookie', models.BooleanField(default=False)),
                ('shoot_catches', models.CharField(max_length=1)),
                ('roster_status', models.CharField(default='N', max_length=1)),
                ('current_team', models.CharField(max_length=50)),
                ('primary_position', models.CharField(max_length=50)),
            ],
        ),
    ]
