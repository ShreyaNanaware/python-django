from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def home(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()

    return render(request, 'event/home.html', {'events': events, 'form': form})

