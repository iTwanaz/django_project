from django.shortcuts import render, redirect
from .forms import (
    UserRegistrationForm, 
    UserUpdateForm, 
    ProfileUpdateForm
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages         #to pass a one time message to the template

# messages.info
# messages.debug
# messages.success
# messages.warning
# messages.error

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, Would you like to Login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()       #creating an instance of UserCreationForm Class
    return render(request, 'users/register.html', {'form': form})       #passing a dictionary as the context


@login_required             #decorator 
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, 
                                instance = request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance = request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)