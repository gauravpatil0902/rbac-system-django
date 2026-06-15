from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class BaseSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            Profile.objects.create(user=user, role=self.role)

        return user


class StudentSignUpForm(BaseSignUpForm):
    role = 'student'


class TeacherSignUpForm(BaseSignUpForm):
    role = 'teacher'


class RegisterForm(BaseSignUpForm):
    role = 'student'
