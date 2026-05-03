from django.contrib import admin
from django.urls import path, include
from suss_project import views

from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),

    # MAIN
    path('', views.dashboard),
    path('dashboard/', views.dashboard),

    # APPS
    path('expenses/', include('expenses.urls')),
    path('notes/', views.notes),
    path('planner/', views.planner),
    path('resume/', views.resume),
]