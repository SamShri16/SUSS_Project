from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
    path('pin/<int:id>/', views.pin_note, name='pin_note'),
]