from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('calc:post_list')
    else:
        form = UserCreationForm()
    return render(request, 'calc/signup.html', {'form': form})

# Log in a user
from django.contrib.auth import logout

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("calc:post_list")  
        return render(request, "calc/login.html", {"form": form, "error": "Invalid credentials"})

    return render(request, "calc/login.html", {"form": AuthenticationForm()})


from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'calc/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'calc/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('calc:post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'calc/post_edit.html', {'form': form})

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    
    if post.author != request.user:
        return HttpResponseForbidden("You are not authorized to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES , instance=post)
        if form.is_valid():
            form.save()
            return redirect('calc:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'calc/post_edit.html', {'form': form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not authorized to delete this post.")

    post.delete()
    return redirect('calc:post_list')


def logout_view(request):
    logout(request)
    return redirect('calc:login')  
