import stripe
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from datetime import datetime

from company.models import FoodHistory
from restaurants.models import *

stripe.api_key = 'sk_test_51PAbDZHo0Q90Btn2ijp84H9gwvIUJqZGtSdJo4VoLCunCsgn9n5PBLibd1Lt3DWzRAT5vdimm2czxDZ2T8ZrzSq300oPBzoNxV'


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    restaurantimage = serializers.SerializerMethodField()
    restaurantoff = serializers.SerializerMethodField()
    restaurant_categories = serializers.SerializerMethodField()

    def get_restaurantoff(self, obj):
        try:
            restaurantoff = obj.restaurantoff
            restaurantoff_serializer = RestaurantOffSerializer(restaurantoff
                                                               )
            return restaurantoff_serializer.data
        except Exception as e:
            pass

    def get_restaurantimage(self, obj):
        restaurantimages = obj.restaurantimage_set.all()
        restaurantimages_serializer = RestaurantImageSerializer(restaurantimages,
                                                                many=True)
        return restaurantimages_serializer.data

    def get_restaurant_categories(self, obj):
        restaurantimages = obj.categories
        restaurantimages_serializer = RestaurantCategorySerializer(restaurantimages,
                                                                   many=True)
        return restaurantimages_serializer.data

    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = '__all__'


class FoodItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemCategory
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


def simple_time_format(time_obj):
    if not time_obj:
        return None

    formatted_time = time_obj.strftime('%I:%M %p')
    return formatted_time.lstrip('0')


class RestaurantScheduleSerializer(serializers.ModelSerializer):
    formatted_open_time = serializers.SerializerMethodField()
    formatted_close_time = serializers.SerializerMethodField()

    class Meta:
        model = RestaurantSchedule
        fields = '__all__'

    def get_formatted_open_time(self, obj):
        return simple_time_format(obj.opening_time)

    def get_formatted_close_time(self, obj):
        return simple_time_format(obj.closing_time)


class RestaurantOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantOff
        fields = '__all__'


class FoodItemSerializer(serializers.ModelSerializer):
    fooditemimage = serializers.SerializerMethodField()
    quantity = serializers.IntegerField(write_only=True)
    food_item_id = serializers.CharField(write_only=True, max_length=10)
    categories = FoodItemCategorySerializer(required=False, many=True)
    ingredients = IngredientSerializer(required=False, many=True)

    def get_fooditemimage(self, obj):
        fooditemimages = obj.fooditemimage_set.all()
        fooditemimages_serializer = FoodItemImageSerializer(fooditemimages,
                                                            many=True)
        return fooditemimages_serializer.data

    def validate(self, attrs):
        # Remove the categories field from the attrs dictionary
        attrs.pop('categories', None)
        return attrs

    class Meta:
        model = FoodItem
        fields = '__all__'


class FoodItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemImage
        fields = '__all__'


class SingleOrderSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(write_only=True, many=True)

    class Meta:
        model = SingleOrder
        fields = '__all__'

    def create(self, validated_data):
        food_items = validated_data.pop('food_items')
        instance = SingleOrder.objects.create(**validated_data)
        line_item = []
        for food_item in food_items:
            print(food_item)
            food_item.pop('description')
            name = food_item.pop('name')
            # food_item.pop('restaurant')
            if food_item.get('allow_discount'):
                food_item['subtotal'] = (int(food_item.get('price')) - (
                        food_item.get('discount') / 100) * int(food_item.get('price'))) * food_item.get('quantity')
            else:
                food_item['subtotal'] = int(food_item.get('price')) * food_item.get('quantity')

            line_item.append({
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(food_item['subtotal']) * 100,
                    "product_data": {
                        "name": name,
                    },
                },
                'quantity': 1,
            })

            food_item.pop('price')
            food_item.pop('allow_discount')
            food_item.pop('discount')
            food_item.pop('ingredients')
            food_item['order'] = instance
            food_item['food_item_id'] = food_item.pop('food_item_id')
            print(food_item)
            SingleOrderItem.objects.create(**food_item)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line_item,
                mode='payment',
                success_url="http://localhost:3000/",
                cancel_url="http://localhost:3000/",
            )
            validated_data['payment_redirect_url'] = checkout_session.url
        except Exception as e:
            print(e)
            return str(e)

        print(validated_data)
        return validated_data


class CateringOrderSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(write_only=True, many=True)

    class Meta:
        model = CateringOrder
        fields = '__all__'

    def create(self, validated_data):
        food_items = validated_data.pop('food_items')
        instance = CateringOrder.objects.create(**validated_data)
        line_item = []
        for food_item in food_items:
            print(food_item)
            food_item.pop('description')
            name = food_item.pop('name')
            # food_item.pop('restaurant')
            if food_item.get('allow_discount'):
                food_item['subtotal'] = (int(food_item.get('price')) - (
                        food_item.get('discount') / 100) * int(food_item.get('price'))) * food_item.get('quantity')
            else:
                food_item['subtotal'] = int(food_item.get('price')) * food_item.get('quantity')

            line_item.append({
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(food_item['subtotal']) * 100,
                    "product_data": {
                        "name": name,
                    },
                },
                'quantity': 1,
            })

            food_item.pop('price')
            food_item.pop('allow_discount')
            food_item.pop('discount')
            food_item.pop('ingredients')
            food_item['order'] = instance
            food_item['food_item_id'] = food_item.pop('food_item_id')
            print(food_item)
            CateringOrderItem.objects.create(**food_item)

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line_item,
                mode='payment',
                success_url="http://localhost:3000/",
                cancel_url="http://localhost:3000/",
            )
            validated_data['payment_redirect_url'] = checkout_session.url
        except Exception as e:
            print(e)
            return str(e)

        print(validated_data.get('food_items'))
        return validated_data


class GroupOrderSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(write_only=True, many=True)
    food_history_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GroupOrder
        fields = '__all__'

    def create(self, validated_data):
        food_items = validated_data.pop('food_items')
        # meal_type = validated_data.pop('meal_type')
        food_history_id = validated_data.pop('food_history_id')
        food_history = FoodHistory.objects.get(id=food_history_id)
        validated_data['teammember'] = self.context.get('request').user
        validated_data['delivered_date'] = food_history.date
        validated_data['delivered_time'] = food_history.time
        instance = GroupOrder.objects.create(**validated_data)
        line_item = []
        for food_item in food_items:
            print(food_item)
            food_item.pop('description')
            name = food_item.pop('name')
            # food_item.pop('restaurant')
            if food_item.get('allow_discount'):
                food_item['subtotal'] = (int(food_item.get('price')) - (
                        food_item.get('discount') / 100) * int(food_item.get('price'))) * food_item.get('quantity')
            else:
                food_item['subtotal'] = int(food_item.get('price')) * food_item.get('quantity')

            line_item.append({
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(food_item['subtotal']) * 100,
                    "product_data": {
                        "name": name,
                    },
                },
                'quantity': 1,
            })

            food_item.pop('price')
            food_item.pop('allow_discount')
            food_item.pop('discount')
            food_item.pop('ingredients')
            food_item['order'] = instance
            food_item['food_item_id'] = food_item.pop('food_item_id')
            food_item['team_member'] = self.context.get('request').user
            print(food_item)
            GroupOrderItem.objects.create(**food_item)

        food_history.is_menu_selected = True
        food_history.save()

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line_item,
                mode='payment',
                success_url="http://localhost:3000/",
                cancel_url="http://localhost:3000/",
            )
            validated_data['payment_redirect_url'] = checkout_session.url
        except Exception as e:
            print(e)
            return str(e)

        print(validated_data.get('food_items'))
        return validated_data


class SingleOrderItemSerializer(serializers.ModelSerializer):
    order = SingleOrderSerializer(read_only=True, many=False)
    food_item = FoodItemSerializer(read_only=True, many=False)

    class Meta:
        model = SingleOrderItem
        fields = '__all__'


class GroupOrderItemSerializer(serializers.ModelSerializer):
    order = GroupOrderSerializer(read_only=True, many=False)
    food_item = FoodItemSerializer(read_only=True, many=False)

    class Meta:
        model = GroupOrderItem
        fields = '__all__'


class CateringOrderItemSerializer(serializers.ModelSerializer):
    order = CateringOrderSerializer(read_only=True, many=False)
    food_item = FoodItemSerializer(read_only=True, many=False)

    class Meta:
        model = CateringOrderItem
        fields = '__all__'
