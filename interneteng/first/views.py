from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm


def home(request):
    # render home page
    return render(request, 'users/home.html')


def contact(request):
    return render(request, 'users/contact.html')


def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        # all requirements (e.g 8characters) are met
        if form.is_valid():
            # save in db
            form.save()
            # get username
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account has been created sucessfully')
            return redirect('home')
        else:
            form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})
