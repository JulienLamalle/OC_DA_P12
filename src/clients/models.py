from django.db import models

from users.models import User


class Client(models.Model):
  first_name = models.CharField(verbose_name='Prenom', max_length=25)
  last_name = models.CharField(verbose_name='Nom', max_length=25)
  email = models.EmailField(
      verbose_name='Adresse email',
      unique=True,
      error_messages={
          'unique': "A client with that email address already exists.",
        },
    )
  phone = models.CharField(
      verbose_name='numero de telephone',
      max_length=20,
      unique=True,
      error_messages={
          'unique': "A client with that phone number already exists.",
        },
    )
  mobile = models.CharField(
      verbose_name='numero de portable',
      max_length=20,
      unique=True,
      error_messages={
          'unique': "A client with that mobile number already exists.",
        },
    )
  company_name = models.CharField(
      verbose_name="nom d'entreprise", max_length=250)
  created_at = models.DateTimeField(verbose_name='cree a', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name="mis a jour a", auto_now=True)
  sales_contact = models.ForeignKey(
      to=User,
      on_delete=models.SET_NULL,
      null=True,
      limit_choices_to={'role': User.SALES},
      error_messages={
          'limit_choices_to': "This user is not part of the sales team.",
        },
      verbose_name='contact commercial',
    )

  class Meta:
    verbose_name = 'client'
    verbose_name_plural = 'clients'

  def __str__(self):
    return f"{self.first_name} {self.last_name} {self.email}"
