from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import NotesDemoForm
from .models import NotesDemo


# Create your views here.


def home(request):

    return render(request, "home.html")


def create_note(request):
    """
    This is the function that controls the create page.
    It is used to create new Notes and save them to the database
    :param request: This is from the website
    :return:
    """
    if request.method == "POST":
        print("ping")
        form = NotesDemoForm(request.POST)
        if form.is_valid():
            print("step 2")
            note = form.save()
            note.save()
    return render(request, "create.html")


def update_note(request, pk):
    """
    This will update the give notes data
    :param request: from the website
    :param pk: this is the id or primary key of the note in the database
    :return:
    """
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
    """
    This is used to delete a given note.

    :param request: I don't know if the function will break if
           I remove this so I leave it iin
    :param pk: This is the primary key or id for the given note
    :return:
    """
    note = get_object_or_404(NotesDemo, pk=pk)
    note.delete()
    return redirect('http://127.0.0.1:8000/list/')


def list_notes(request):
    """
    This is to list all the notes that are in the database
    :param request:
    :return:
    """

    notes = NotesDemo.objects.all()
    return render(request, "list.html", {'notes': notes})
