from django.contrib import admin
from reviews.models import *
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "fooditem", "comment", "rating", "date_time")

class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ("id", "review", "image")

def _register(model, admin_class):
    admin.site.register(model, admin_class)
_register(Review, ReviewAdmin)
_register(ReviewImage, ReviewImageAdmin)