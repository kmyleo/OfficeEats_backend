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