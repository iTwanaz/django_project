from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()       #creating an instance of UserCreationForm Class
    return render(request, users/register.html, {'form': form})       #oassing a dictionary as the context
