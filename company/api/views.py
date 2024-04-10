from rest_framework import viewsets
from company.api.serializers import *
from company.models import *

class CompanyModelViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TeamModelViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamMemberModelViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamRuleModelViewSet(viewsets.ModelViewSet):
    queryset = TeamRule.objects.all()
    serializer_class = TeamRuleSerializer