from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from expenses.models import Expense
from notes.models import Note
from planner.models import Task
from django.contrib import messages

@login_required
def dashboard(request):
    total_expense = sum(e.amount for e in Expense.objects.all())
    pending_tasks = Task.objects.filter(completed=False)
    pinned_notes = Note.objects.filter(pinned=True)[:3]

    return render(request, 'dashboard.html', {
        'total_expense': total_expense,
        'pending_tasks_count': pending_tasks.count(),
        'pending_tasks': pending_tasks[:3],   # 🔥 NEW
        'pinned_notes': pinned_notes
    })


@login_required
def expense(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        Expense.objects.create(amount=amount, category=category)

    expenses = Expense.objects.all()
    return render(request, 'expense.html', {'expenses': expenses})


@login_required
def delete_expense(request, id):
    Expense.objects.get(id=id).delete()
    return redirect('/expenses/')


@login_required
def notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)

    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})


@login_required
def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect('/notes/')


@login_required
def pin_note(request, id):
    note = Note.objects.get(id=id)

    if Note.objects.filter(pinned=True).count() < 3:
        note.pinned = True
        note.save()

    return redirect('/notes/')


@login_required
def planner(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        Task.objects.create(title=title, date=date)

    tasks = Task.objects.all()
    return render(request, 'planner.html', {'tasks': tasks})


@login_required
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return redirect('/planner/')


@login_required
def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/planner/')


@login_required
def resume(request):
    score = None

    if request.method == 'POST':
        resume = request.POST.get('resume', '').lower()
        skills = request.POST.get('skills', '').split(',')

        count = 0
        for s in skills:
            if s.strip().lower() in resume:
                count += 1

        if len(skills) > 0:
            score = (count / len(skills)) * 100

    return render(request, 'resume.html', {'score': score})