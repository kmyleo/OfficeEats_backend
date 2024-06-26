# Generated by Django 5.0 on 2024-04-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0039_cateringorder_payment_redirect_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="grouporder",
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
