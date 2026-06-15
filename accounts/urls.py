from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path('signup/student/', views.student_signup, name='student_signup'),
    path('signup/teacher/', views.teacher_signup, name='teacher_signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('manager-page/', views.manager_page, name='manager_page'),
    path('user-page/', views.user_page, name='user_page'),
    path('teachers/', views.teacher_page, name='teacher_page'),
    path('students/', views.student_page, name='student_page'),
]
