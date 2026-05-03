from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner, name='planner'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
]