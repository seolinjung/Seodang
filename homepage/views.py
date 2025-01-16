from django.shortcuts import render, redirect
from .models import Input
from django.http import HttpResponse

from .forms import InputForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = InputForm()
    return render(request, 'homepage/homepage.html', {"form": form})

def result(request):
    return HttpResponse("result")