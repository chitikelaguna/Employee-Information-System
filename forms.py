from django import forms
from .models import employee2

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee2
        fields = '__all__'