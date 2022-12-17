from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ...


class Computer(models.Model):
    name = models.CharField(max_length=100)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="computers"
    )
