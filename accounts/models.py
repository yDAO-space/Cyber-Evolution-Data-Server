from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    display_name = models.CharField("Отображаемое имя", max_length=150, blank=True)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)

    def __str__(self):
        return self.display_name or self.username