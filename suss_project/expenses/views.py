from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Expense, Income


@login_required
def expenses_view(request):
    filter_type = request.GET.get('filter', 'all')

    today = date.today()

    if filter_type == 'today':
        expenses = Expense.objects.filter(user=request.user, date=today)

    elif filter_type == 'week':
        start_week = today - timedelta(days=7)
        expenses = Expense.objects.filter(user=request.user, date__gte=start_week)

    elif filter_type == 'month':
        expenses = Expense.objects.filter(user=request.user, date__month=today.month)

    else:
        expenses = Expense.objects.filter(user=request.user)

    expenses = expenses.order_by('-date')

    total_expense = sum(e.amount for e in expenses)

    return render(request, 'expenses.html', {
        'expenses': expenses,
        'total_expense': total_expense,
        'filter': filter_type
    })


@login_required
def add_expense(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        date_val = request.POST.get("date")

        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            date=date_val
        )

    return redirect('expenses')


@login_required
def add_income(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        source = request.POST.get("source")
        date_val = request.POST.get("date")

        Income.objects.create(
            user=request.user,
            amount=amount,
            source=source,
            date=date_val
        )

    return redirect('expenses')