from django.contrib import admin
from django import forms

from users.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email',
              'first_name', 'last_name', 'role']

  def save(self, commit=True):
    user = super(UserForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password'])
    if self.cleaned_data['role'] == 'management':
      user.is_staff = True
      user.is_superuser = True
    if commit:
      user.save()
    return user

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  form = UserForm
  list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role')
  list_filter = ('role',)
  search_fields = ('username', 'email', 'first_name', 'last_name')
  ordering = ('username',)
  list_per_page = 30