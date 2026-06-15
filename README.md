# Django School Role Based Authentication System

This is a simple beginner-friendly school-style RBAC project using Django built-in authentication.

## Features

- Student and teacher sign up pages
- User login and logout
- Three roles: Admin, Teacher, Student
- Dashboard shows links based on account type
- Admin-only page
- Teacher-only page
- Student-only page
- SQLite database

## Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open this URL:

```text
http://127.0.0.1:8000/
```

## Optional Admin Account

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```
