from django.shortcuts import render, reverse, redirect
from CASCASE.utils import get_user


def home_page(request):
    context = {}

    user = get_user(request, context)

    if user is None:
        return redirect(reverse("trending:trending"))

    return render(request, "home/index.html", context)

