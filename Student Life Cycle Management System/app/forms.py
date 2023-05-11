"""
Definition of forms.
"""

from email.policy import default
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Subject, Registration

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class StudentLogin(forms.Form):
    reg_no = forms.IntegerField(label="Registration Number: ")
    pswd = forms.CharField(widget = forms.PasswordInput, label = "Password: ")

class SubjectSelectionForm(forms.ModelForm):
    # define the choices field as a MultipleChoiceField with ChoiceInput widgets
    choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        choices=Subject.CHOICES,
        required=False,
    )

    def clean_choices(self):
        # check that at most MAX_CHOICES options are selected
        choices = self.cleaned_data['choices']
      
        #if len(choices) > Subject.MAX_CHOICES:
        #   raise forms.ValidationError(f'You can select up to {Subject.MAX_CHOICES} subjects.')
        return choices

    class Meta:
        model = Subject
        fields = ('choices',)