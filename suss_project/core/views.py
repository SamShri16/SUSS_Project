from django.shortcuts import render
from expenses.models import Expense
from planner.models import Task


def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')

    expenses = Expense.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user)

    total_expense = sum(e.amount for e in expenses)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    context = {
        'total_expense': total_expense,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'recent_tasks': tasks.order_by('-id')[:5],
        'recent_expenses': expenses.order_by('-id')[:5],
    }

    return render(request, 'core/dashboard.html', context)