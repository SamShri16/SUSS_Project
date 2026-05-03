from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_view, name='expenses'),

    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('income/', views.income_view, name='income'),

    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
]