# Generated by Django 3.0.7 on 2020-06-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('venue_name', models.CharField(max_length=50)),
                ('abbrevation', models.CharField(max_length=3)),
                ('first_year_of_play', models.CharField(max_length=4)),
                ('division', models.CharField(max_length=50)),
                ('conference', models.CharField(max_length=50)),
                ('official_site', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='primary_number',
            field=models.CharField(max_length=3),
        ),
    ]
