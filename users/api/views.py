import json

import requests
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from company.models import TeamMember
from restaurants.models import Restaurant
from users.models import User
from .serializers import UserSerializer
from ..filters import UserApiFilter

def get_ip_info(request):
    data = {}
    try:
        response = requests.get(
            "https://geolocation-db.com/json/")
        data_string = response.content.decode('utf-8')
        data = json.loads(data_string)
    except Exception as e:
        print(e)
    return JsonResponse(data)

class UserCreateAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    filterset_class = UserApiFilter

    def get_queryset(self):
        team_members = [i.user.id for i in
                        TeamMember.objects.filter(team_id=self.request.query_params.get('teammember__team__id'))]
        queryset = User.objects.all().exclude(id__in=team_members)
        return queryset


class LoggedInUserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        restaurant = Restaurant.objects.filter(user=request.user).first()
        data = serializer.data
        data['id'] = request.user.pk
        data['restaurant_id'] = restaurant.id if restaurant else None
        return Response(data)
