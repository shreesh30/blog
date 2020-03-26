from django.shortcuts import render
from blogapp.models import Post,Comments
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def blog(request):
    posts=Post.objects.all().order_by('created_on')
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'posts':paged_posts
    }
    return render(request,'blog/blog.html',context)


def post(request,blog_id):
    post_details=get_object_or_404(Post,pk=blog_id)
    comments=Comments.objects.all().filter(post=post_details)
    context={
        'post_details':post_details,
        'comments':comments,
        # id:blog_id
    }
    return render(request,'blog/post.html',context)

