# Generated by Django 5.0 on 2024-03-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0019_alter_restaurantschedule_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="singleorder",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Placed", "Placed"),
                    ("Delivered", "Delivered"),
                    ("Cancelled", "Cancelled"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
    ]