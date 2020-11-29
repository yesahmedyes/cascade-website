from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user_name = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Undefined'),
        ('A', 'Attack helicopter'),
        ('N', 'Super nonconforming asexual reverse trans optic gender')
    )
    gender = models.CharField(max_length=1, choices=gender_choices)


class Follower(models.Model):
    follower = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='follower_person')
    following = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='following_person')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='follower_constraint')
        ]
