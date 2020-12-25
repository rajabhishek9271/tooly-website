from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RecruiterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields = ('username', 'email', 'password')
        labels = {

        'email': _("Company Email")
        }
