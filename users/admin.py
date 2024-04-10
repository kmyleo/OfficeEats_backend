from django.contrib import admin
from users.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "phone_number", "address", "is_partner")


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(User, UserAdmin)