from django.contrib import admin
from django.urls import path, include

from accounts.views import login_view, register_view, logout_view
from core.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # DASHBOARD
    path('', dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),

    # APPS
    path('expenses/', include('expenses.urls')),
    path('notes/', include('notes.urls')),
    path('planner/', include('planner.urls')),
    path('resume/', include('resume.urls')),
]