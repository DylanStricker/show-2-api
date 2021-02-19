from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Show(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  description = models.CharField(max_length=100, blank=True)
  director = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      null=True,
      on_delete=models.SET_NULL
  )
  def __str__(self):
    # This must return a string
    return f"The show {self.title}'s average rating is {self.rating} and was directed by {self.director}"

  def as_dict(self):
    """Returns dictionary version of Show models"""
    return {
        'id': self.id,
        'title': self.title,
        'rating': self.rating,
        'description': self.description,
        'director': self.director,
        'owner': self.owner,
        'users': self.users
    }
