from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def home(request):
    context = {

    }
    return render(request, "index.html", context)


def signup(request):
    if request.method == "POST":
        print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login/")

    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "register.html", context)
