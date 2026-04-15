from django.shortcuts import render
from .models import Note
from django.contrib.auth.decorators import login_required

@login_required
def notes_view(request):
    if request.method == "POST":
        Note.objects.create(
            user=request.user,
            title=request.POST['title'],
            content=request.POST['content']
        )

    data = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'data': data})