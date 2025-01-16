from django.shortcuts import render
from .models import Input

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', {})