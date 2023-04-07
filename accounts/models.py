from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _
# from .managers import UserManager
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username=None
    # email=models.EmailField(max_length=254)
    email=models.EmailField(max_length=254,unique=True)
    mobile=models.CharField(max_length=50,unique=True)
    is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    forget_password=models.CharField(max_length=100,null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)

    # ________________________________________________________________________________________
    #  IF we want mobile number during admin login
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    # objects= UserManager()
    # USERNAME_FIELD='email'
    
    # USERNAME_FIELD='mobile'
    # REQUIRED_FIELDS=[]


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['mobile']

