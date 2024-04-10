from django.db import models

from users.models import User


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)


class TeamRule(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    budget_per_order = models.IntegerField()
    order_per_day = models.IntegerField()
