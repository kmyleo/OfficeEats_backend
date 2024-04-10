from rest_framework import viewsets
from reviews.api.serializers import *
from reviews.models import *
from reviews.filters import *

class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewApiFilter