# Generated by Django 5.0 on 2024-01-17 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurantimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_off', models.BooleanField(default=False)),
                ('discount', models.IntegerField(null=True)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
