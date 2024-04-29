from django_filters import rest_framework as filters, FilterSet, CharFilter
from restaurants.models import *


class FoodItemApiFilter(filters.FilterSet):
    category_ids = CharFilter(method='filter_by_category_ids')

    class Meta:
        model = FoodItem
        fields = {
            "restaurant_id": ['exact'],
        }

    def filter_by_category_ids(self, queryset, name, value):
        category_ids = [int(i) for i in value.split(',')]
        queryset = queryset.filter(categories__id__in=category_ids)
        return queryset


class RestaurantApiFilter(filters.FilterSet):
    category_ids = CharFilter(method='filter_by_category_ids')

    class Meta:
        model = Restaurant
        fields = {
            "business_name": ['icontains'],
            "restauranttype__type": ['iexact'],
            "restauranttype__people_from_range": ['gte'],
            "restauranttype__people_to_range": ['lte'],
        }

    def filter_by_category_ids(self, queryset, name, value):
        category_ids = [int(i) for i in value.split(',')]
        queryset = queryset.filter(categories__id__in=category_ids)
        return queryset


class RestaurantScheduleApiFilter(filters.FilterSet):
    class Meta:
        model = RestaurantSchedule
        fields = {
            "restaurant_id": ['exact'],
        }


class SingleOrderApiFilter(filters.FilterSet):
    class Meta:
        model = SingleOrder
        fields = {
            "customer_id": ['exact'],
            "singleorderitem__restaurant__user_id": ['exact'],
        }


class GroupOrderApiFilter(filters.FilterSet):
    class Meta:
        model = GroupOrder
        fields = {
            "teammember_id": ['exact'],
            "grouporderitem__restaurant__user_id": ['exact'],
        }


class CateringOrderApiFilter(filters.FilterSet):
    class Meta:
        model = CateringOrder
        fields = {
            "customer_id": ['exact'],
            "cateringorderitem__restaurant__user_id": ['exact'],
        }


class SingleOrderItemApiFilter(filters.FilterSet):
    class Meta:
        model = SingleOrderItem
        fields = {
            "order_id": ['exact'],
        }


class GroupOrderItemApiFilter(filters.FilterSet):
    class Meta:
        model = GroupOrderItem
        fields = {
            "order_id": ['exact'],
        }


class CateringOrderItemApiFilter(filters.FilterSet):
    class Meta:
        model = CateringOrderItem
        fields = {
            "order_id": ['exact'],
        }
