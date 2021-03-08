from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from .show import Show
from .viewer import Viewer

class Comment(models.Model):
  value = models.CharField(max_length=3000)
  owner = models.ForeignKey(
      Viewer,
      on_delete=models.CASCADE
  )
  show = models.ForeignKey(
      Show,
      on_delete=models.CASCADE
  )

  def __str__(self):
    """Return a string version of Comment model"""
    # This must return a string
    return f"The Comment, {self.value} on {self.show} by {self.owner}"

  def as_dict(self):
    """Returns dictionary version of Viewer model"""
    return {
        'id': self.id,
        'value': self.value,
        'show': self.show,
        'owner': self.owner
    }
