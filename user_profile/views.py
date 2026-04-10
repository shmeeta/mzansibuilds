from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import UserProfile
from .forms import ProfileUpdateForm
# Create your views here.

@login_required(login_url="/login") 
def user_profile(request, username):
    user_to_view = get_object_or_404(User, username=username)
    user_projects= user_to_view.project_set.all().order_by('-created_at')
    return render(request, 'user_profile/profile.html', {
        'profile_user': user_to_view, 
        'projects': user_projects
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
      
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'user_profile/edit_profile.html', {'form': form})