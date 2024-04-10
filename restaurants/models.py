from django.db import models
from django.utils.translation import gettext_lazy as _
from company.models import Company, Team
from users.models import User


# Create your models here.

class Restaurant(models.Model):
    business_name = models.CharField(max_length=200)
    website_url = models.URLField(max_length=2000, null=True)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField("RestaurantCategory")


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField()


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=100)


class FoodItemCategory(models.Model):
    name = models.CharField(max_length=100)


class RestaurantSchedule(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    FROM_DATE_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
    ]
    TO_DATE_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
    ]
    STATUS_CHOICES = [
        ('OPENING', 'Opening'),
        ('CLOSED', 'Closed'),
    ]
    from_date = models.CharField(max_length=20, choices=FROM_DATE_CHOICES, default="Monday")
    to_date = models.CharField(max_length=20, choices=TO_DATE_CHOICES, default="Saturday")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Opening")


class RestaurantOff(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    allow_off = models.BooleanField(default=False)
    discount = models.IntegerField(null=True)


# class RestaurantImage(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     image = models.ImageField()

class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    allow_discount = models.BooleanField(default=False)
    discount = models.IntegerField(null=True)
    categories = models.ManyToManyField("FoodItemCategory")

    def __str__(self):
        return self.name


class FoodItemImage(models.Model):
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    image = models.ImageField()


class SingleOrder(models.Model):
    class Status(models.TextChoices):
        Pending = 'Pending', _('Pending')
        Placed = 'Placed', _('Placed')
        Delivered = 'Delivered', _('Delivered')
        Cancelled = 'Cancelled', _('Cancelled')

    status = models.CharField(max_length=20, choices=Status, default=Status.Pending)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.email}"


class GroupOrder(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class SingleOrderItem(models.Model):
    order = models.ForeignKey(SingleOrder, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)


class GroupOrderItem(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PLACED', 'Placed'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    order = models.ForeignKey(GroupOrder, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
