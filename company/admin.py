from django.contrib import admin
from company.models import *


class FoodHistoryAdmin(admin.ModelAdmin):
    list_display = ("teammember", "team_rule", "date", "time", "set_away", "type")


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(FoodHistory, FoodHistoryAdmin)
