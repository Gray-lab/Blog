from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=64, unique=True)
  content = models.TextField()
  date_created = models.DateTimeField(auto_now_add = True)
  date_modified = models.DateTimeField(auto_now = True)

  def __str__(self):
    return f'{self.title} written on {self.date_created}'

