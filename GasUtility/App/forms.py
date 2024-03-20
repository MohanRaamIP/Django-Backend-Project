from django import forms
from .models import service

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = service
        fields = ['name', 'service_request', 'status']
