from django.shortcuts import render, redirect
from .forms import RegisterForm, ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Project

@login_required(login_url="/login")
def home(request):
    projects = Project.objects.all()
    if request.method == "POST":
        project_id = request.POST.get("project-id")
        project = Project.objects.filter(id=project_id).first()
        if project and project.author == request.user: 
            project.delete()
    return render(request, 'main/home.html', {"projects":projects})

def sign_up(request): 
    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        # make a new user 
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            return redirect('/home')

    else: 
        form = RegisterForm() 
    return render(request, 'registration/sign_up.html', {"form": form })


def logOut(request): 
    logout(request)
    return redirect("/login")

@login_required(login_url="/login")
def create_project(request): 
    if request.method == 'POST': 
        form = ProjectForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else: 
        form = ProjectForm() 
    
    return render(request, 'main/create_project.html', {"form":form})

