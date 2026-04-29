from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_view, name='expenses'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
]