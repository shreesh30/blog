from django.shortcuts import render
from blogapp.models import Post 
# from django.http import HttpResponse
# Create your views here.
def index(request):
    posts=Post.objects.all().order_by('-created_on')
    context={
        'posts':posts,
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')