from django import forms
from student.models import Profile
class Registration(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name', 'email' ,'password', 'age', 'city']
        widgets={
            'password':forms.PasswordInput()
        }