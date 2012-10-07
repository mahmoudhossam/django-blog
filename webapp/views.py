from django.template.response import TemplateResponse
from models import Post
from forms import *
from util import *
from django.views.decorators.http import require_http_methods, require_GET
from django.shortcuts import redirect

@require_http_methods(['GET', 'POST'])
def new_post(request):
    if request.method == 'GET':
        return TemplateResponse(request, 'new.html', context={'form': PostForm()})
    else:
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            text = post_form.cleaned_data['text']
            return create_post(title, text)

@require_GET
def all_posts(request):
    posts = Post.objects.all()
    return TemplateResponse(request, 'posts.html', context={'posts': posts})

@require_GET
def single_post(request, year, month, day, slug):
    post = get_post(year, month, day, slug)
    return TemplateResponse(request, 'post.html', context={'post': post})

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return TemplateResponse(request, 'signup.html',
        context={'form': SignupForm()})
    else:
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            username = signupform.cleaned_data['username']
            email = signupform.cleaned_data['email']
            password = signupform.cleaned_data['password']
            create_user(username, email, password)
            return redirect('/')
