from django.urls import path
from . import views
urlpatterns=[
    path('<int:blog_id>',views.blog,name='blog'),
    # path('post/<int:blog_id>')
]