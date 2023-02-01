from django import forms
from app.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'dob', 'email_id', 'Phone_no']