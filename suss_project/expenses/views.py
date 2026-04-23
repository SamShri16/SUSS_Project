from django.shortcuts import render, redirect
from .models import Expense, Income
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date


@login_required
def expense_view(request):

    filter_type = request.GET.get('filter')

    # ✅ ONLY CURRENT USER DATA
    expenses = Expense.objects.filter(user=request.user)

    if filter_type == 'today':
        expenses = expenses.filter(date=date.today())

    elif filter_type == 'month':
        expenses = expenses.filter(date__month=date.today().month)

    total = sum(e.amount for e in expenses)

    if request.method == 'POST':
        Expense.objects.create(
            user=request.user,   # ✅ IMPORTANT
            amount=request.POST.get('amount'),
            category=request.POST.get('category'),
            date=request.POST.get('date')
        )

        messages.success(request, "Expense added")
        return redirect('/expenses/')

    return render(request, 'expense.html', {
        'expenses': expenses,
        'total': total
    })


@login_required
def delete_expense(request, id):
    Expense.objects.filter(id=id, user=request.user).delete()  # ✅ SAFE DELETE
    messages.success(request, "Expense deleted")
    return redirect('/expenses/')


@login_required
def income_view(request):

    incomes = Income.objects.filter(user=request.user)

    total_income = sum(i.amount for i in incomes)

    if request.method == 'POST':
        Income.objects.create(
            user=request.user,  # ✅ IMPORTANT
            amount=request.POST.get('amount'),
            source=request.POST.get('source'),
            date=request.POST.get('date')
        )

        messages.success(request, "Income added")
        return redirect('/income/')

    return render(request, 'income.html', {
        'incomes': incomes,
        'total_income': total_income
    })