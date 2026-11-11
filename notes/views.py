from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def index(request):
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:index")
    else:
        form = NoteForm()
    
    return render(
        request, 
        "notes/note_form.html", 
        {"form": form, "title": "Новая заметка"}
    )


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:index")
    else:
        form = NoteForm(instance=note)
        
    return render(
        request, 
        "notes/note_form.html", 
        {"form": form, "title": "Редактирование"}
    )


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("notes:index")
        
    return render(
        request, 
        "notes/note_confirm_delete.html", 
        {"note": note}
    )