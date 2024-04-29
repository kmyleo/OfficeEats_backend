from django_filters import rest_framework as filters, FilterSet, CharFilter
from company.models import *


class TeamApiFilter(filters.FilterSet):
    class Meta:
        model = Team
        fields = {
            "user_id": ['exact'],
            "teammember__user__id": ['exact'],
        }


class TeamMemberApiFilter(filters.FilterSet):
    class Meta:
        model = TeamMember
        fields = {
            "team__id": ['exact'],
        }


class TeamRuleApiFilter(filters.FilterSet):
    class Meta:
        model = TeamRule
        fields = {
            "team__id": ['exact'],
            "team__teammember__user__id": ['exact'],
        }


class FoodHistoryApiFilter(filters.FilterSet):
    class Meta:
        model = FoodHistory
        fields = {
            "teammember__team__id": ['exact'],
            "teammember__user__id": ['exact'],
            "date": ['exact'],
            "is_menu_selected": ['exact'],
        }
