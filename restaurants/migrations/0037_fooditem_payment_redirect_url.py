# Generated by Django 5.0 on 2024-04-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0036_alter_cateringorderitem_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="fooditem",
            name="payment_redirect_url",
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
    ]
