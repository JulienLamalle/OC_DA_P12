from django.db import models

from clients.models import Client
from users.models import User
from contracts.models import Contracts


class Event(models.Model):
  title = models.CharField(verbose_name='titre', max_length=250)
  support_contact = models.ForeignKey(
    to=User,
    on_delete=models.SET_NULL,
    null=True,
    limit_choices_to={'role': User.SUPPORT},
    error_messages={
      'limit_choices_to': "This user is not part of the support team.",
    },
    verbose_name='contact support'
  )
  contract = models.ForeignKey(
    to=Contracts,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name='contrat',
  )
  is_finished = models.BooleanField(verbose_name='est termine', default=False)
  event_date = models.DateTimeField(verbose_name='date de l\'evenement')
  attendees = models.IntegerField(verbose_name='nombre de participants')
  notes = models.TextField(verbose_name='notes', blank=True, null=True)
  created_at = models.DateTimeField(verbose_name='cree a', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='mis a jour a', auto_now=True)

  class Meta:
    verbose_name = 'evenement'
    verbose_name_plural = 'evenements'

  def __str__(self):
    return f"{self.title}"

  def client(self):
    if self.contract:
      return self.contract.client
