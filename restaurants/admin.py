from django.contrib import admin
from restaurants.models import *


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "business_name", "website_url", "phone_number", "address", "city", "user")


class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "image")


class RestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class FoodItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class RestaurantScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "id", "restaurant", "description", "opening_time", "closing_time", "FROM_DATE_CHOICES", "TO_DATE_CHOICES",
        "STATUS_CHOICES", "from_date", "to_date", "status")


class RestaurantOffAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "allow_off", "discount")


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "name", "description", "price", "allow_discount", "discount")


class FoodItemImageAdmin(admin.ModelAdmin):
    list_display = ("id", "fooditem", "image")


class SingleOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "customer", "order_date", "total_amount")


class CateringOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "customer", "no_of_peoples", "order_date", "total_amount")


class GroupOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id", "team", 'teammember', "order_date", 'delivered_date', 'delivered_time', 'meal_type', "total_amount")


class SingleOrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "food_item", "quantity", "subtotal")


class CateringOrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "food_item", "quantity", "subtotal")


class GroupOrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "order", "food_item", "quantity", "subtotal", "team_member")


class RestaurantTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "type", "people_from_range", "people_to_range")


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Restaurant, RestaurantAdmin)
_register(RestaurantImage, RestaurantImageAdmin)
_register(RestaurantCategory, RestaurantCategoryAdmin)
_register(FoodItemCategory, FoodItemCategoryAdmin)
_register(RestaurantSchedule, RestaurantScheduleAdmin)
_register(RestaurantOff, RestaurantOffAdmin)
_register(FoodItem, FoodItemAdmin)
_register(FoodItemImage, FoodItemImageAdmin)
_register(SingleOrder, SingleOrderAdmin)
_register(CateringOrder, CateringOrderAdmin)
_register(GroupOrder, GroupOrderAdmin)
_register(SingleOrderItem, SingleOrderItemAdmin)
_register(CateringOrderItem, CateringOrderItemAdmin)
_register(GroupOrderItem, GroupOrderItemAdmin)
_register(Ingredient, IngredientAdmin)
_register(RestaurantType, RestaurantTypeAdmin)
