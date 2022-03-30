from django.contrib import admin
from django import forms

# models
from events.models import Event
from clients.models import Client


class ClientFilter(admin.SimpleListFilter):
  title = 'client'
  parameter_name = 'client'

  def lookups(self, request, model_admin):
    return Client.objects.values_list('company_name', 'company_name')

  def queryset(self, request, queryset):
    if self.value():
      return queryset.filter(contract__client__company_name=self.value())
    return queryset


class EventForm(forms.ModelForm):

  class Meta:
    model = Event
    fields = (
        "title", 'contract', 'support_contact', 'event_date', 'is_finished',
        'attendees', 'notes'
    )

  def save(self, commit=True):

    event = super().save(commit=False)
    if commit:
      event.save()
    return event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

  form = EventForm
  list_display = (
      'id', 'title', 'contract', 'support_contact', 'event_date', 'is_finished',
      'attendees', 'notes'
  )
  search_fields = ('title',)
  list_filter = (ClientFilter, 'contract', 'support_contact', 'is_finished')
  autocomplete_fields = ('contract', 'support_contact')
  list_per_page = 30

  def has_add_permission(self, request):
    return False

  def has_delete_permission(self, request, obj=None):
    return False
