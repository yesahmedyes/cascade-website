from django.contrib import admin
from .models import Person, Follower


admin.site.register(Person)
admin.site.register(Follower)