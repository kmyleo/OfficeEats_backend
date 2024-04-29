from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class TeamRule(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    allow_breakfast = models.BooleanField(default=False)
    allow_lunch = models.BooleanField(default=False)
    allow_dinner = models.BooleanField(default=False)
    breakfast_budget = models.IntegerField(default=0)
    lunch_budget = models.IntegerField(default=0)
    dinner_budget = models.IntegerField(default=0)
    breakfast_time = models.TimeField(default='09:00:00')
    lunch_time = models.TimeField(default='14:00:00')
    dinner_time = models.TimeField(default='21:00:00')


class FoodHistory(models.Model):
    class Type(models.TextChoices):
        Breakfast = 'Breakfast', _('Breakfast')
        Lunch = 'Lunch', _('Lunch')
        Dinner = 'Dinner', _('Dinner')

    teammember = models.ForeignKey(TeamMember, on_delete=models.CASCADE, null=True)
    team_rule = models.ForeignKey(TeamRule, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    set_away = models.BooleanField(default=False)
    is_menu_selected = models.BooleanField(default=False)
    type = models.CharField(max_length=200, choices=Type.choices, null=True)
