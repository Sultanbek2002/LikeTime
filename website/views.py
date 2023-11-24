from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
teachers=Teachers.objects.all()
cours=Cours.objects.all()
def index(request):
    context={
        "teachers":teachers,
        "cours": cours
    }
    return render(request,'website/index.html',context)
def blog(request):
    return render(request, 'website/blog.html')