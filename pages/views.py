from django.shortcuts import render
from blogapp.models import Post 
# from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')