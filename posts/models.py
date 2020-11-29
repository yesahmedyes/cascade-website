from django.db import models
from user.models import Person


class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    votes = models.IntegerField(default=0, null=False, blank=False)


class Like(models.Model):
    vote_choices = (
        (1, 'upvote'),
        (-1, 'downvote')
    )
    vote = models.CharField(max_length=1, choices=vote_choices, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='Like_Constraint')
        ]


class Comment(models.Model):
    comment = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
