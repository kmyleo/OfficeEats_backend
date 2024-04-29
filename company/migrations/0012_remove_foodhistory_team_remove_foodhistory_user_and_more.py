# Generated by Django 5.0 on 2024-04-24 14:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0011_foodhistory_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foodhistory",
            name="team",
        ),
        migrations.RemoveField(
            model_name="foodhistory",
            name="user",
        ),
        migrations.AddField(
            model_name="foodhistory",
            name="teammember",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
