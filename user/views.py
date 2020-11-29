from django.shortcuts import render, reverse, redirect, HttpResponse
from CASCASE.utils import get_user, get_posts
from .models import Follower
from user.models import Person
from django.template.loader import render_to_string


app_name = "user"


def my_profile(request, slug=None):
    context = {}
    user = me = None

    if slug is None or slug is user:
        user = get_user(request, context)
    else:
        me = get_user(request, context)
        if me.user_name == slug:
            user = me
            me = slug = None
        else:
            user = Person.objects.get(user_name=slug)

    if user is None:
        return redirect(reverse("trending:trending"))

    posts = get_posts(user)
    print("posts", posts)

    data = {
        'name': user.first_name + " " + user.last_name,
        'username': user.user_name,
        'image': user.image,
        'posts': posts,
        'post_count': len(posts),
        'follower_count': Follower.objects.filter(following=user).count(),
        'following_count': Follower.objects.filter(follower=user).count(),
        'myprofile': (slug is None),
        'following': (Follower.objects.filter(follower=me, following=user).exists()) if me is not None else False,
    }

    context.update(data)

    return render(request, 'profile/profile.html', context)


def follow_person(request):
    if request.is_ajax():
        context = {}

        get_to_follow = request.POST.get("username" or None)
        to_follow = Person.objects.get(user_name=get_to_follow)
        user = get_user(request, context)

        follow, created = Follower.objects.get_or_create(follower=user, following=to_follow)

        if not created:
            follow.delete()

        return HttpResponse(status=204)


def get_followers(request):
    if request.is_ajax():
        username = request.POST.get("username")
        type = request.POST.get("type")
        user = Person.objects.get(user_name=username)

        context = {
            'people': Follower.objects.filter(following=user) if type == "followers" else Follower.objects.filter(follower=user),
            'type': type
        }
        template = render_to_string("profile/person_card.html", context=context)

        return HttpResponse(template)








