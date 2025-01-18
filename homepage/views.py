from django.shortcuts import render, redirect
from .models import Input
from django.http import HttpResponse

from .forms import InputForm

from langdetect import detect
import homepage.to_hanja as to_hanja 

# Create your views here.
def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            input = form.save()
            # print(type(form.text))
            detect_result = detect(input.text)
            output = ''
            if (detect_result != 'ko'):
                output = "The sentence you entered is not in Korean. Refresh this page." 
            else:
                output = to_hanja.convert_sentence(input.text)
                broken_pairs = to_hanja.break_down(input.text, output)



            return render(request, 'homepage/result.html', {"origin": input.text, "result": output})
            # return redirect('result')
    else:
        form = InputForm()
    return render(request, 'homepage/homepage.html', {"form": form})

