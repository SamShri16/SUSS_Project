from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def planner_view(request):
    if request.method == "POST":
        Task.objects.create(
            user=request.user,
            title=request.POST['title'],
            deadline=request.POST['deadline']
        )

    data = Task.objects.filter(user=request.user)
    return render(request, 'planner.html', {'data': data})