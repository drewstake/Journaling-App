from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms

from .models import JournalEntry

def home(request):
    entries = []
    if request.user.is_authenticated:
        entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'home/home.html', {
        'entries': entries,
        'today': timezone.now().date(),
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

class EntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        form = EntryForm()
    return render(request, 'home/entry_form.html', {'form': form})