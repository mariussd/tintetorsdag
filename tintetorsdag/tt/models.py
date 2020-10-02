from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    @property
    def is_tinting(self):
        return self.tints().filter(created=date.today()).exists()

    def tints(self):
        return Tint.objects.filter(user=self)


class Tint(models.Model):
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
