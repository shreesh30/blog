from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.blog,name='post_list'),
    path('<int:blog_id>',views.post,name='post'),
    # path('post/<int:blog_id>')
]