from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField, Sum, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for techno_q26_backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    email = EmailField(_('email address'), blank=False, unique=True)
    first_name = CharField(_('first name'), max_length=200)
    last_name = CharField(_('first name'), max_length=200)
    phone_number = CharField(_('phone_number'), max_length=200)
    address = CharField(_('Address'), max_length=200)
    is_partner = BooleanField(_('Is Partner'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


