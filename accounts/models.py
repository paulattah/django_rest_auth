from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=256, unique=True, verbose_name=_("Email Address"))
    first_name=models.TextField(max_lenght=60, verbose_name=_("First Name"))
    last_name=models.TextField(max_lenght=60, verbose_name=_("Last Name"))
    is_staff =models.BooleanField(default=False)
    is_active =models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELDS = "email"

    REQUIRED_FIELDS =["first_name", "last_name"]

    objects = UserManger()\
    
    def __str__(self):
        return self.email
    
    #function to get fullname
    def get_full_name(self):
        return f"{self.first_name} {self. last_name}" 
    

    
        