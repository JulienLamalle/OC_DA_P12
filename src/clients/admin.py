from django.contrib import admin

from django.contrib import admin
from django import forms

# models
from clients.models import Client


class ClientForm(forms.ModelForm):

  class Meta:
    model = Client
    fields = (
      'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact'
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
  form = ClientForm
  list_display = (
    "id", 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact'
  )

  search_fields = (
    'first_name', 'last_name', 'email', 'company_name'
  )
  list_filter = ('sales_contact',)
  autocomplete_fields = ('sales_contact',)
  list_per_page = 30

  def has_add_permission(self, request):
    return False

  def has_delete_permission(self, request, obj=None):
    return False
