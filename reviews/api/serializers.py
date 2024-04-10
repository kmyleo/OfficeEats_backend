from rest_framework import serializers
from rest_framework.exceptions import NotFound

from reviews.models import *
from users.api.serializers import *

class ReviewSerializer(serializers.ModelSerializer):
    reviewimage = serializers.SerializerMethodField()
    def get_reviewimage(self, obj):
        reviewimages = obj.reviewimage_set.all()
        reviewimages_serializer = ReviewImageSerializer(reviewimages,
                                                                many=True)
        return reviewimages_serializer.data
    class Meta:
        model = Review
        fields = '__all__'

    user_data = serializers.SerializerMethodField()

    def get_user_data(self, obj):
        try:
            user_data = obj.user
            user_data_serializer = UserSerializer(user_data
                                                  )
            return user_data_serializer.data
        except Exception as e:
            pass

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = '__all__'