from models import *
from datetime import date
from django.shortcuts import redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

def create_post(title, text):
    post_date = date.today()
    slug = slugify(title)
    post = Post(title=title, text=text, created_at=post_date, slug=slug)
    post.save()
    return redirect('/')

def get_post(year, month, day, slug):
    year, month, day = map(int, (year, month, day))
    post_date = date(year, month, day)
    post = get_object_or_404(Post, created_at=post_date)
    return post

def create_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    return user