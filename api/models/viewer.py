from django.db import models
from django.contrib.auth.models import User
from .show import Show
class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shows = models.ManyToManyField(Show)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        """Return a string version of Viewer model"""
        # This must return a string
        return f"The Viewer, {self.user} (or {self.nickname})'s  shows are {self.shows}"

    def as_dict(self):
        """Returns dictionary version of Viewer model"""
        return {
            'id': self.id,
            'shows': self.shows,
            'user': self.user,
            'nickname': self.nickname
        }
