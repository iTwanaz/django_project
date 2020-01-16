from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
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
