from django.shortcuts import HttpResponse
from posts.models import Post, Like, Comment
from user.models import Person
from django.template.loader import render_to_string
import json


def update_post(request):
    if request.is_ajax():
        user = request.POST.get("user")
        post = int(request.POST.get("post"))
        val = int(request.POST.get("value"))

        my_post = Post.objects.get(pk=post)
        my_user = Person.objects.get(pk=user)
        like, new_like = Like.objects.get_or_create(post=my_post, user=my_user)
        context = {}

        if new_like:
            like.vote = val
            my_post.votes += val
            like.save()
        else:
            old_val = int(like.vote)
            if old_val == val:
                my_post.votes -= old_val
                like.delete()
            else:
                my_post.votes = my_post.votes - old_val + val
                like.vote = val
                like.save()

        my_post.save()
        context.update({'votes': my_post.votes})

        return HttpResponse(json.dumps(context), content_type="application/json")


def fetch_comments(request):
    if request.is_ajax():
        user = request.POST.get("user")
        post = request.POST.get("post")

        context = {
            'comments': Comment.objects.filter(post=post)
        }
        template = render_to_string("posts/comments.html", context=context)

        return HttpResponse(template)
