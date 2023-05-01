"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class StudentLogin(forms.Form):
    reg_no = forms.IntegerField(Label="Registration Number: ")
    pswd = forms.CharField(widget = forms.PasswordInput, label = "Password: ")

