from rest_framework import serializers

from company.models import *
from users.api.serializers import UserSerializer
from datetime import date, timedelta


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        instance = Team.objects.create(**validated_data)
        team_rule_instance = TeamRule.objects.create(team=instance)

        return instance


class TeamMemberSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = TeamMember
        fields = '__all__'

    def create(self, validated_data):
        instance = TeamMember.objects.create(**validated_data)
        print(instance.team.teamrule_set.first())
        if instance.team.teamrule_set.first().allow_breakfast:
            today = date.today()
            for i in range(30):
                new_date = today + timedelta(days=i)
                FoodHistory.objects.create(teammember=instance,
                                           team_rule=instance.team.teamrule_set.first(),
                                           date=new_date,
                                           time=instance.team.teamrule_set.first().breakfast_time,
                                           type='Breakfast')

        if instance.team.teamrule_set.first().allow_lunch:
            today = date.today()
            for i in range(30):
                new_date = today + timedelta(days=i)
                FoodHistory.objects.create(teammember=instance,
                                           team_rule=instance.team.teamrule_set.first(),
                                           date=new_date,
                                           time=instance.team.teamrule_set.first().lunch_time,
                                           type='Lunch')

        if instance.team.teamrule_set.first().allow_dinner:
            today = date.today()
            for i in range(30):
                new_date = today + timedelta(days=i)
                FoodHistory.objects.create(teammember=instance,
                                           team_rule=instance.team.teamrule_set.first(),
                                           date=new_date,
                                           time=instance.team.teamrule_set.first().dinner_time,
                                           type='Dinner')
        return instance


class TeamRuleSerializer(serializers.ModelSerializer):
    team_detail = serializers.SerializerMethodField()

    def get_team_detail(self, obj):
        team_data = obj.team
        team_data_serializer = TeamSerializer(team_data, many=False)
        return team_data_serializer.data

    class Meta:
        model = TeamRule
        fields = '__all__'


class FoodHistorySerializer(serializers.ModelSerializer):
    team_member_detail = serializers.SerializerMethodField()
    team_rule_detail = serializers.SerializerMethodField()

    def get_team_member_detail(self, obj):
        team_data = obj.teammember
        team_data_serializer = TeamMemberSerializer(team_data, many=False)
        return team_data_serializer.data

    def get_team_rule_detail(self, obj):
        team_data = obj.team_rule
        team_data_serializer = TeamRuleSerializer(team_data, many=False)
        return team_data_serializer.data

    class Meta:
        model = FoodHistory
        fields = '__all__'
