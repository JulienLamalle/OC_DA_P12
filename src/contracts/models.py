from django.db import models

from users.models import User
from clients.models import Client


class Contracts(models.Model):
  client = models.ForeignKey(
      to=Client,
      on_delete=models.CASCADE,
      verbose_name='client'
    )
  sales_contact = models.ForeignKey(
      to=User,
      on_delete=models.SET_NULL,
      null=True,
      limit_choices_to={'role': User.SALES},
      error_messages={
          'limit_choices_to': "This user is not part of the sales team.",
        },
      verbose_name='sales contact'
    )
  created_at = models.DateTimeField(verbose_name='cree a', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='mis a jour a', auto_now=True)
  amount = models.IntegerField(verbose_name="montant")
  payment_due_date = models.DateTimeField(verbose_name='date de paiement')
  is_signed = models.BooleanField(verbose_name='est signe', default=False)
  is_paid = models.BooleanField(verbose_name="est payé", default=False)

  class Meta:
    verbose_name = 'contrat'
    verbose_name_plural = 'contrats'

  def __str__(self):
    return f"{self.client.first_name} {self.client.last_name} - {self.amount} - {self.created_at.strftime('%d/%m/%Y')}"
