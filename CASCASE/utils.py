from django.db import connection
from user.models import Person
from collections import namedtuple
from CASCASE.settings import MEDIA_URL


def get_posts(user=None, me=None):
    with connection.cursor() as cursor:
        if user is None:
            query = f"SELECT * FROM posts_post"
        else:
            if me is None:
                me = user
            query = f"SELECT * FROM posts_post LEFT JOIN posts_like ON posts_post.id = posts_like.post_id WHERE posts_post.user_id='{user.user_name}'"
        cursor.execute(query)
        Post = namedtuple('Post', 'id content image username votes vote')
        d = []
        for each in cursor.fetchall():
            if user is None:
                post = Post(each[0], each[1], MEDIA_URL + each[2], each[3], each[4], 0)
            else:
                post = Post(each[0], each[1], MEDIA_URL + each[2], each[3], each[4], each[6])
            d.append(post)
    return d


def get_user(request, context):
    if request.user.is_authenticated:
        username = request.user.username
        user, _ = Person.objects.get_or_create(pk=username)
        context.update({'my_username': username})
        context.update({'my_image': user.image})
        return user
    else:
        return None
