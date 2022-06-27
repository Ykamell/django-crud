from django import forms
from .models import Users

class DateInput(forms.DateInput):
    input_type = 'date'

class TextInput(forms.TextInput):
    input_type = 'text'

class UsersForms(forms.ModelForm):
        
    class Meta:
        model = Users
        fields = '__all__'
        widgets = {
            'Name': TextInput(),
            'Lastname': TextInput(),
            'Birthday': DateInput(),
        }