# Generated by Django 5.0 on 2024-04-24 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0006_remove_teamrule_budget_per_order_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="budget",
        ),
        migrations.RemoveField(
            model_name="teammember",
            name="address",
        ),
        migrations.RemoveField(
            model_name="teammember",
            name="budget",
        ),
    ]
