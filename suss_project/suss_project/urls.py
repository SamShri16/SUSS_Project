"""
URL configuration for suss_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as acc
from expenses.views import expense_view
from notes.views import notes_view
from planner.views import planner_view
from resume.views import resume_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', acc.login_view, name='login'),
    path('register/', acc.register_view, name='register'),
    path('dashboard/', acc.dashboard_view, name='dashboard'),
    path('logout/', acc.logout_view, name='logout'),

    path('expenses/', expense_view, name='expenses'),
    path('notes/', notes_view, name='notes'),
    path('planner/', planner_view, name='planner'),
    path('resume/', resume_view, name='resume'),
]