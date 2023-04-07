from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.backends import BaseBackend
##  IF we want email  during admin login
# class UserManager(BaseUserManager):
#     use_in_migrations=True


#     def create_user(self,email,password=None,**extra_fields):

#         if not email:
#             raise ValueError("Email is require")
        
#         email=self.normalize_email(email)
#         user=self.model(email=email,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self,email,password,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         if extra_fields.get('is_staff') is not True:
#             raise  ValueError(('Super User must have is_staff true'))
        
#         return self.create_user(email,password,**extra_fields)



# #  IF we want mobile number during admin login
# class CustomUserManager(BaseUserManager):
#     def create_user(self, mobile, password=None, **extra_fields):
#         user = self.model(mobile=mobile, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, mobile, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(mobile, password, **extra_fields)





# If we want to login admin either by email or by mobile no.then:
# class CustomUserManager(BaseUserManager):
#     def _get_user_by_email_or_mobile(self, email_or_mobile):
#         try:
#             user = self.get(email=email_or_mobile)
#         except self.model.DoesNotExist:
#             try:
#                 user = self.get(mobile=email_or_mobile)
#             except self.model.DoesNotExist:
#                 return None
#         return user

#     def authenticate(self, request, email_or_mobile=None, password=None, **kwargs):
#         user = self._get_user_by_email_or_mobile(email_or_mobile)
#         if user and user.check_password(password):
#             return user
#         return None

#     def create_user(self, mobile, password=None, **extra_fields):
#         user = self.model(mobile=mobile, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, mobile, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(mobile, password, **extra_fields)



# if we want to login admin by mobile,email,password then:
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    A custom user manager to use email and mobile as the authentication fields.
    """

    def authenticate(self, request, email=None, mobile=None, password=None, **kwargs):
        """
        Authenticate a user based on email and mobile.
        """
        try:
            user = self.get(email=email)
        except self.model.DoesNotExist:
            try:
                user = self.get(mobile=mobile)
            except self.model.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None

    def create_user(self, email=None, mobile=None, password=None, **kwargs):
        """
        Create and save a User with the given email and password.
        """
        if not email and not mobile:
            raise ValueError('Users must have an email address or mobile number')

        user = self.model(email=self.normalize_email(email), mobile=mobile, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, mobile=None, password=None, **kwargs):
        """
        Create and save a SuperUser with the given email and password.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email=email, mobile=mobile, password=password, **kwargs)
