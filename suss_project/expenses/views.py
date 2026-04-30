from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from datetime import date


@login_required
def expense_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        expense_date = request.POST.get("date")

        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            date=expense_date if expense_date else date.today()
        )

        return redirect("expenses")

    expenses = Expense.objects.filter(user=request.user).order_by("-date")

    return render(request, "expenses/expenses.html", {
        "expenses": expenses
    })


@login_required
def delete_expense(request, id):
    exp = Expense.objects.get(id=id, user=request.user)
    exp.delete()
    return redirect("expenses")


@login_required
def income_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        source = request.POST.get("source")
        income_date = request.POST.get("date")

        Income.objects.create(
            user=request.user,
            amount=amount,
            source=source,
            date=income_date if income_date else date.today()
        )

        return redirect("income")

    incomes = Income.objects.filter(user=request.user).order_by("-date")

    return render(request, "expenses/income.html", {
        "incomes": incomes
    })


from django.http import HttpResponse

def add_expense(request):
    return HttpResponse("Add Expense Page")



