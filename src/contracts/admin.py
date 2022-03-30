from django.contrib import admin
from django import forms

# models
from contracts.models import Contracts


class ContractForm(forms.ModelForm):

  class Meta:

    model = Contracts
    fields = (
      'client', 'amount', 'payment_due_date', 'is_signed', 'is_paid',
    )

  def save(self, commit=True):
    contract = super().save(commit=False)
    contract.sales_contact = self.cleaned_data['client'].sales_contact
    if commit:
      contract.save()
    return contract


@admin.register(Contracts)
class ContractAdmin(admin.ModelAdmin):

  form = ContractForm
  list_display = (
    'id', 'client', 'sales_contact', 'amount', 'payment_due_date', 'is_signed', 'is_paid'
  )
  search_fields = ('client',)
  list_filter = ('client', 'sales_contact', 'is_paid', 'is_signed')
  autocomplete_fields = ('client', 'sales_contact',)
  list_per_page = 30

  def has_add_permission(self, request):
    return False

  def has_delete_permission(self, request, obj=None):
    return False
