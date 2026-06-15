from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import RegisterForm, StudentSignUpForm, TeacherSignUpForm


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm


def register(request):
    return redirect('signup')


def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'accounts/signup.html')


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Student account created successfully.')
            return redirect('dashboard')
    else:
        form = StudentSignUpForm()

    return render(request, 'accounts/student_signup.html', {'form': form})


def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Teacher account created successfully.')
            return redirect('dashboard')
    else:
        form = TeacherSignUpForm()

    return render(request, 'accounts/teacher_signup.html', {'form': form})


@login_required
def dashboard(request):
    role = get_role(request.user)
    return render(request, 'accounts/dashboard.html', {'role': role})


@login_required
def admin_page(request):
    if get_role(request.user) != 'admin':
        messages.error(request, 'Only admin users can open that page.')
        return redirect('dashboard')
    return render(request, 'accounts/admin_page.html')


@login_required
def manager_page(request):
    return redirect('teacher_page')


@login_required
def teacher_page(request):
    if get_role(request.user) not in ['admin', 'teacher']:
        messages.error(request, 'Only teachers can open that page.')
        return redirect('dashboard')
    return render(request, 'accounts/teacher_page.html')


@login_required
def user_page(request):
    return redirect('student_page')


@login_required
def student_page(request):
    if get_role(request.user) not in ['admin', 'student']:
        messages.error(request, 'Only students can open that page.')
        return redirect('dashboard')
    return render(request, 'accounts/student_page.html')


def get_role(user):
    if user.is_superuser:
        return 'admin'
    return user.profile.role
