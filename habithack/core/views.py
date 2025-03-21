from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def habits(request):
    return render(request, 'navici.html')

def rewards(request):
    return render(request, 'prizes.html')