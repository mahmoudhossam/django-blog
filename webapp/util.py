from models import *
from datetime import date
from django.shortcuts import redirect

def new_post(title, text):
    post_date = date.today()
    post = Post(title=title, text=text, created_at=post_date)
    post.save()
    return redirect('/')
