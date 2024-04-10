from django_filters import rest_framework as filters, FilterSet, CharFilter
from reviews.models import *


class ReviewApiFilter(filters.FilterSet):
    class Meta:
        model = Review
        fields = {
            "fooditem__restaurant_id": ['exact'],
        }
