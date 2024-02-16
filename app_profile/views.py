from django.contrib.auth import login
from django.shortcuts import render, redirect

from app_profile.forms import RegisterForm


# Create your views here.
def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,
                  'registration/registration.html',
                  {'form': form})

