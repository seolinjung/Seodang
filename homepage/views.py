from django.shortcuts import render, redirect
from .models import Input
from django.http import HttpResponse

from .forms import InputForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form_data = form.save()
            
            return render(request, 'homepage/result.html', {"result": form_data})
            # return redirect('result')
    else:
        form = InputForm()
    return render(request, 'homepage/homepage.html', {"form": form})

def result(request):
    # return render(request, 'hompage/results.html', {"result", form.cleaned_data})
    # recent_sentence = Input.objects.filter()

     return HttpResponse("result")