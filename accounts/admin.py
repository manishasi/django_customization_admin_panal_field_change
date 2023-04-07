# from django.contrib import admin
# from .models import *
# @admin.register(CustomUser)
# class CustomuserAdmin(admin.ModelAdmin):
#     list_display=('id','mobile','email','forget_password','password')
# # your_virtualenv_directory/lib/python3.9/site-packages/django/contrib/admin/templates/admin/login.html
# 

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
from .forms import CustomAuthenticationForm
# from .models import CustomUser



from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import *
@admin.register(CustomUser)
class CustomuserAdmin(admin.ModelAdmin):
    list_display=('id','mobile','email','forget_password','password')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'admin/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('admin:index')


class CustomAdminSite(admin.AdminSite):
    login_form = CustomLoginView


admin_site = CustomAdminSite()

