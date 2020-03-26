from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=225)
    body=models.TextField()
    created_on=models.DateField(auto_now_add=True,blank=True)
    last_modified=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='photos/%Y/%m',blank=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        return self.title

class Comments(models.Model):
    author=models.CharField(max_length=60)
    body=models.TextField()
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    def __str__(self):
        return self.author
