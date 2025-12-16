from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import NotesDemoForm
from .models import NotesDemo


# Create your views here.


def home(request):

    return render(request, "home.html")


def create_note(request):
    if request.method == "POST":
        print("ping")
        form = NotesDemoForm(request.POST)
        if form.is_valid():
            print("step 2")
            note = form.save()
            note.save()
    return render(request, "create.html")


def update_note(request, pk):
    note = get_object_or_404(NotesDemo, pk=pk)
    if request.method == "POST":
        form = NotesDemoForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/list/')

    if request.method == "DELETE":
        note.delete()
        return redirect('http://127.0.0.1:8000/list/')

    notes = NotesDemo.objects.filter(id=pk)
    return render(request, "update.html", {'notes': notes})


def delete_note(request, pk):
    note = get_object_or_404(NotesDemo, pk=pk)
    note.delete()
    return redirect('http://127.0.0.1:8000/list/')


def list_notes(request):

    notes = NotesDemo.objects.all()
    return render(request, "list.html", {'notes': notes})
