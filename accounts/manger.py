from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManger(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("please enter a valid email"))
        
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if email:
            email= self.normalize_email(email)
            self.email_validator(email)

        else:
            raise ValueError(_("an email address is required"))
        
        if not first_name:
            raise ValueError(_("first name is required"))
        if not last_name:
            raise ValueError(_("last name is required"))
        
        user =self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.save(using=self._db)

        return user
    
    def create_superuser
