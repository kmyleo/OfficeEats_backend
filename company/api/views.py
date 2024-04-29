from django.db.models import Max, F
from rest_framework import viewsets
from company.api.serializers import *
from company.filters import TeamApiFilter, TeamMemberApiFilter, TeamRuleApiFilter, FoodHistoryApiFilter
from company.models import *


class CompanyModelViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TeamModelViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamApiFilter


class TeamMemberModelViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filterset_class = TeamMemberApiFilter


class TeamRuleModelViewSet(viewsets.ModelViewSet):
    # queryset = TeamRule.objects.all().order_by('-id')
    serializer_class = TeamRuleSerializer
    filterset_class = TeamRuleApiFilter

    def get_queryset(self):
        # Annotate the latest record for each team
        queryset = TeamRule.objects.annotate(
            latest_id=Max('team__teamrule__id')
        ).filter(id=F('latest_id'))
        return queryset


class FoodHistoryModelViewSet(viewsets.ModelViewSet):
    queryset = FoodHistory.objects.all()
    serializer_class = FoodHistorySerializer
    filterset_class = FoodHistoryApiFilter
