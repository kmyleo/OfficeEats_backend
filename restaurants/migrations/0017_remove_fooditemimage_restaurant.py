# Generated by Django 5.0 on 2024-01-25 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0016_fooditemimage_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditemimage',
            name='restaurant',
        ),
    ]
