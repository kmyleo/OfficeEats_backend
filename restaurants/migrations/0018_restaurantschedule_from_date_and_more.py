# Generated by Django 5.0 on 2024-03-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0017_remove_fooditemimage_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantschedule',
            name='from_date',
            field=models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='Monday', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurantschedule',
            name='status',
            field=models.CharField(choices=[('OPENING', 'Opening'), ('CLOSING', 'Closing')], default='Opening', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurantschedule',
            name='to_date',
            field=models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='Saturday', max_length=20),
        ),
    ]
