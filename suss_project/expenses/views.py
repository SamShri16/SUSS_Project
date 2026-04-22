from django.shortcuts import render, redirect
from .models import Expense, Income
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date


@login_required
def expense_view(request):

    filter_type = request.GET.get('filter')

    expenses = Expense.objects.all()

    # ✅ FILTER LOGIC
    if filter_type == 'today':
        expenses = expenses.filter(date=date.today())

    elif filter_type == 'month':
        expenses = expenses.filter(date__month=date.today().month)

    total = sum(e.amount for e in expenses)

    # ✅ ADD EXPENSE
    if request.method == 'POST':
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        exp_date = request.POST.get('date')

        Expense.objects.create(
            amount=amount,
            category=category,
            date=exp_date
        )

        messages.success(request, "Expense added")
        return redirect('/expenses/')

    return render(request, 'expense.html', {
        'expenses': expenses,
        'total': total
    })


@login_required
def delete_expense(request, id):
    Expense.objects.get(id=id).delete()
    messages.success(request, "Expense deleted")
    return redirect('/expenses/')


# 💰 INCOME
@login_required
def income_view(request):

    incomes = Income.objects.all()
    total_income = sum(i.amount for i in incomes)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        source = request.POST.get('source')
        inc_date = request.POST.get('date')

        Income.objects.create(
            amount=amount,
            source=source,
            date=inc_date
        )

        messages.success(request, "Income added")
        return redirect('/income/')

    return render(request, 'income.html', {
        'incomes': incomes,
        'total_income': total_income
    })