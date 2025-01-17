from django.shortcuts import render, redirect
from .models import Input
from django.http import HttpResponse

from .forms import InputForm

import homepage.to_hanja as to_hanja 

# Create your views here.
def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            input = form.save()
            # print(type(form.text))
            output = to_hanja.convert_sentence(input.text)
            return render(request, 'homepage/result.html', {"result": output})
            # return redirect('result')
    else:
        form = InputForm()
    return render(request, 'homepage/homepage.html', {"form": form})

def result(request):
    # return render(request, 'hompage/results.html', {"result", form.cleaned_data})
    # recent_sentence = Input.objects.filter()

     return HttpResponse("result")