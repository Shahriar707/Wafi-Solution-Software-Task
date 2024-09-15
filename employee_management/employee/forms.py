from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}))
    
    class Meta:
        
        model = Employees
        fields = ['full_name', 'email', 'mobile', 'date_of_birth', 'photos']