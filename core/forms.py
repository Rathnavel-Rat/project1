"""
WSGI config for Project1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
from django import forms
from .models import reg
class Enter(forms.ModelForm):
	class Meta:
		model=reg
		fields="__all__"
		widgets = { 'Value': forms.TextInput(attrs={'size': 120})}
	