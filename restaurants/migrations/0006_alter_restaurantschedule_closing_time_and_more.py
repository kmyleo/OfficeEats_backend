# Generated by Django 5.0 on 2024-01-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantschedule',
            name='closing_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='restaurantschedule',
            name='opening_time',
            field=models.TimeField(),
        ),
    ]
