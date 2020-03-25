from django.shortcuts import render
from blogapp.models import Post,Comments
from django.shortcuts import get_object_or_404
# Create your views here.
def blog(request,blog_id):
    post_details=get_object_or_404(Post,pk=blog_id)
    comments=Comments.objects.all().filter(post=post_details)
    context={
        'post_details':post_details,
        'comments':comments,
        # id:blog_id
    }
    return render(request,'blog/blog.html',context)



