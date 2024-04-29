from django.contrib.auth import get_user_model
from rest_framework import serializers

from restaurants.api.serializers import RestaurantCategorySerializer, RestaurantSerializer
from restaurants.models import Restaurant, RestaurantCategory
from users.models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    website_url = serializers.URLField(required=False, allow_blank=True)
    business_name = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    business_address = serializers.CharField(required=False, allow_blank=True)
    business_phone_number = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)
    categories = serializers.CharField(required=False, allow_blank=True)

    # categories = RestaurantCategorySerializer(many=True, write_only=True, validators=[])
    # categories = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'business_name', 'password', 'website_url', 'phone_number',
            'address',
            'city', 'is_partner', 'username', 'business_address', 'business_phone_number', 'categories')

    def create(self, validated_data):
        print(validated_data)
        business_name = validated_data.pop("business_name")
        categories = validated_data.pop("categories")
        city = validated_data.pop("city")
        business_address = validated_data.pop("business_address")
        business_phone_number = validated_data.pop("business_phone_number")
        website_url = validated_data.pop("website_url") if validated_data.get("website_url") else None
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if validated_data.get('is_partner', True):
            print("jdjsdjsldjlsld")
            restaurant = Restaurant.objects.create(phone_number=business_phone_number, business_name=business_name,
                                                   address=business_address, website_url=website_url, user=user,
                                                   city=city)
            for i in categories.split(","):
                restaurant.categories.add(int(i))
        return user

    def validate(self, attrs):
        print(attrs)
        if attrs.get('is_partner', True):
            restaurant_data = {
                "business_name": attrs.get("business_name"),
                "city": attrs.get("city"),
                "address": attrs.get("business_address"),
                "phone_number": attrs.get("business_phone_number"),
                "website_url": attrs.get("website_url") if attrs.get("website_url") else None,
                "categories": attrs.get("categories").split(',') if attrs.get("categories") else None,
            }
            serializer = RestaurantSerializer(data=restaurant_data)  # Use RestaurantSerializer
            serializer.is_valid(raise_exception=True)

        return attrs
