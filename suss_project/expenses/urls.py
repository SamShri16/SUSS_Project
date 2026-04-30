from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.expense_view, name='expenses'),
    path('expenses/', include('expenses.urls')),

    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
      # if exists
    path('expenses/', include('expenses.urls')),   # ✅ THIS ONE

    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
]