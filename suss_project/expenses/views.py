from django.shortcuts import render
from .models import Expense
from django.contrib.auth.decorators import login_required

@login_required
def expense_view(request):
    if request.method == "POST":
        Expense.objects.create(
            user=request.user,
            amount=request.POST['amount'],
            category=request.POST['category']
        )

    data = Expense.objects.filter(user=request.user)
    return render(request, 'expense.html', {'data': data})