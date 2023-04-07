# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import BaseModelForm
# from django.utils.translation import ugettext_lazy as _
# from .models import CustomUser


# class CustomAuthenticationForm(BaseModelForm):
#     """
#     A custom authentication form for the Django admin panel.
#     """

#     password = ReadOnlyPasswordHashField(label=_('Password'), help_text=_(
#         'Raw passwords are not stored, so there is no way to see this user\'s password, '
#         'but you can change the password using <a href=\'../password/\'>this form</a>.'))
    
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password','mobile')
#         base_fields = '__all__'


from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form to use email and mobile fields.
    """
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    mobile = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()

    def clean(self):
        email = self.cleaned_data.get('email')
        mobile = self.cleaned_data.get('mobile')
        self.cleaned_data['username'] = email or mobile
        return super().clean()
