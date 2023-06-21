from django.contrib.auth.models import AbstractUser
from django.db import models

class Player(AbstractUser):
    score = models.IntegerField(default=0)
    level = models.CharField(max_length=50)

    # Additional fields and methods can be added based on your requirements

    def __str__(self):
        return self.username