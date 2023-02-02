from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<b>Hello!!</b>")

def index1(request):
    return render(request, "FIRSTAPPLICATION/index.html")