# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Attendance, LeaveRequest

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_admin']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['entry_time', 'exit_time']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['date', 'reason']
