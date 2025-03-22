from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def habits(request):
    return render(request, 'navici.html')

def rewards(request):
    return render(request, 'prizes.html')
    
import random
from django.shortcuts import get_object_or_404, redirect, render
from .models import Habit, Reward
from .forms import HabitForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def habits(request):
    habits = Habit.objects.all()

    habit_name = request.POST.get('habit_name')

    if habit_name:  # Basic check that something was submitted
        Habit.objects.create(name=habit_name)
        return redirect('habits')  # Refresh the page after submission
    
    return render(request, 'navici.html', {
        'habits': habits
    })

def delete_habit(request, id):
    habit = get_object_or_404(Habit, id=id)
    if request.method == 'POST':
        habit.delete()
        return redirect('habits')  # Redirect after deletion

    return redirect('habits')

def rewards(request):
    return render(request, 'prizes.html')