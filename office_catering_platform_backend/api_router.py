from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from restaurants.api.views import *
from company.api.views import *
from reviews.api.views import *

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('restaurant', RestaurantModelViewSet, basename='restaurant')
router.register('restaurant_category', RestaurantCategoryModelViewSet, basename='restaurant_category')
router.register('fooditem_category', FoodItemCategoryModelViewSet, basename='fooditem_category')
router.register('restaurant_schedule', RestaurantScheduleModelViewSet, basename='restaurant_schedule')
router.register('fooditem', FoodItemModelViewSet, basename='fooditem')
router.register('singleorder', SingleOrderModelViewSet, basename='singleorder')
router.register('grouporder', GroupOrderModelViewSet, basename='grouporder')
router.register('singleorderitem', SingleOrderItemModelViewSet, basename='singleorderitem')
router.register('grouporderitem', GroupOrderItemModelViewSet, basename='grouporderitem')

router.register('company', CompanyModelViewSet, basename='company')
router.register('team', TeamModelViewSet, basename='team')
router.register('teamMember', TeamMemberModelViewSet, basename='teamMember')
router.register('teamRule', TeamRuleModelViewSet, basename='teamRule')

router.register('review', ReviewModelViewSet, basename='review')

app_name = "api"
urlpatterns = router.urls
