from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from user.models import Person


@csrf_protect
def login_page(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(reverse("home:home"))
    else:
        return redirect(reverse("trending:trending"))


@csrf_protect
def logout_page(request):
    logout(request)
    return redirect(reverse("trending:trending"))


@csrf_protect
def signup(request):

    return render(request, "auth/signup.html")


@csrf_protect
def register(request):
    email = request.POST.get("email" or None)
    user = request.POST.get("username" or None)
    password = request.POST.get("password" or None)

    if User.objects.filter(username=user).exists() or User.objects.filter(email=email).exists():
        pass
    else:
        new_user = User.objects.create(username=user, email=email)
        new_user.set_password(password)
        new_user.save()
        new_profile = Person.objects.create(user_name=user)
        new_profile.save()
        return redirect(reverse("trending:trending"))


