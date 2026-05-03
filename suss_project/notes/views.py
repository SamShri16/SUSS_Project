from django.shortcuts import render, redirect
from .models import Note

def notes(request):
    all_notes = Note.objects.all().order_by('-id')
    return render(request, 'notes.html', {'notes': all_notes})


def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/notes/')


def pin_note(request, id):
    note = Note.objects.get(id=id)
    note.pinned = not note.pinned
    note.save()
    return redirect('/notes/')