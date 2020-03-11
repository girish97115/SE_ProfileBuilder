from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from profiles.models import StudentProfile, FacultyProfile, Appointment

User = get_user_model()


class DatePickerCustom(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'is_teacher', 'password1', 'password2']


class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        widgets = {'my_date_field': DatePickerCustom()}
        date = forms.DateField()
        fields = ['date']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['image', 'about']


class FacultyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        about = forms.CharField(widget=CKEditorWidget(), label="body")
        articles = forms.CharField(widget=CKEditorWidget(), label="body")
        projects = forms.CharField(widget=CKEditorWidget(), label="body")
        fields = ['image', 'about', 'articles', 'projects', 'interests']
