from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager


class User(AbstractUser):
  MANAGEMENT = 'management'
  SALES = 'sales'
  SUPPORT = 'support'
  
  ROLE_CHOICES = [
    (MANAGEMENT, 'management'),
    (SALES, 'sales'),
    (SUPPORT, 'support')
  ]

  role = models.CharField(
    ('role'), choices=ROLE_CHOICES, blank=True, null=True, max_length=50)

  object = UserManager()

  class Meta:
    verbose_name = ('user')
    verbose_name_plural = ('users')
    ordering = ["role"]
