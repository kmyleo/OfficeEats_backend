# Generated by Django 5.0 on 2024-04-24 13:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0008_teamrule_breakfast_time_teamrule_dinner_time_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="teamrule",
            name="breakfast_time",
            field=models.TimeField(default="09:00:00"),
        ),
        migrations.AlterField(
            model_name="teamrule",
            name="dinner_time",
            field=models.TimeField(default="21:00:00"),
        ),
        migrations.AlterField(
            model_name="teamrule",
            name="lunch_time",
            field=models.TimeField(default="14:00:00"),
        ),
        migrations.CreateModel(
            name="FoodHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(null=True)),
                ("time", models.TimeField(null=True)),
                ("set_away", models.BooleanField(default=False)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="company.team"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
