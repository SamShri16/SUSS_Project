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

from suss_project import views   # MAIN APP VIEWS
from accounts.views import login_view, register_view, logout_view

from expenses.views import expense_view, delete_expense, income_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),

    # MAIN PAGES
    path('', views.dashboard),
    path('dashboard/', views.dashboard),

    path('expenses/', views.expense),
    path('delete-expense/<int:id>/', views.delete_expense),

    path('notes/', views.notes),
    path('delete-note/<int:id>/', views.delete_note),
    path('pin-note/<int:id>/', views.pin_note),

    path('planner/', views.planner),
    path('delete-task/<int:id>/', views.delete_task),
    path('complete-task/<int:id>/', views.complete_task),
    
    path('expenses/', expense_view),
    path('delete-expense/<int:id>/', delete_expense),
    path('income/', income_view),

    path('resume/', views.resume),
]