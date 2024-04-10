from rest_framework import viewsets
from restaurants.api.serializers import *
from restaurants.filters import FoodItemApiFilter, RestaurantApiFilter, RestaurantScheduleApiFilter
from restaurants.models import *


class RestaurantModelViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantApiFilter


class RestaurantCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer

class FoodItemCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = FoodItemCategory.objects.all()
    serializer_class = FoodItemCategorySerializer

class RestaurantScheduleModelViewSet(viewsets.ModelViewSet):
    queryset = RestaurantSchedule.objects.all()
    serializer_class = RestaurantScheduleSerializer
    filterset_class = RestaurantScheduleApiFilter

class FoodItemModelViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    filterset_class = FoodItemApiFilter

class FoodItemImageModelViewSet(viewsets.ModelViewSet):
    queryset = FoodItemImage.objects.all()
    serializer_class = FoodItemImageSerializer

class SingleOrderModelViewSet(viewsets.ModelViewSet):
    queryset = SingleOrder.objects.all()
    serializer_class = SingleOrderSerializer


class GroupOrderModelViewSet(viewsets.ModelViewSet):
    queryset = GroupOrder.objects.all()
    serializer_class = GroupOrderSerializer


class SingleOrderItemModelViewSet(viewsets.ModelViewSet):
    queryset = SingleOrderItem.objects.all()
    serializer_class = SingleOrderItemSerializer


class GroupOrderItemModelViewSet(viewsets.ModelViewSet):
    queryset = GroupOrderItem.objects.all()
    serializer_class = GroupOrderItemSerializer
