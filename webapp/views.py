from django.template.response import TemplateResponse
from models import Post
from forms import *
from util import *

def new_post(request):
    if request.method == 'GET':
        return TemplateResponse(request, 'new.html', context={'form':PostForm()})
    elif request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('/')
