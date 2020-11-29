from django.shortcuts import render
from posts.models import Post
from CASCASE.utils import get_posts


def trending_page(request):
    # if request.user.is_authenticated:
    #     pass
    # else:
    context = {
        'posts': get_posts()
    }
    return render(request, "landing_page.html", context=context)

