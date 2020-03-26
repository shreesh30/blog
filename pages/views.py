from django.shortcuts import render
from blogapp.models import Post
 
# from django.http import HttpResponse
# Create your views here.
def index(request):
    recent_posts=Post.objects.all().order_by('-created_on')[:3]
    context={
        'recent_posts':recent_posts
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')