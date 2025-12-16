from django import forms
from .models import NotesDemo


class NoteForm(forms.Form):
    label = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    content = forms.CharField(max_length=150)
    date = forms.DateField()


class NotesDemoForm(forms.ModelForm):
    class Meta:
        model = NotesDemo
        fields = ['label', 'first_name', 'last_name', 'content', 'date']
