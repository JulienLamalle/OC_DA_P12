# Generated by Django 4.0.3 on 2022-03-11 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='titre')),
                ('is_finished', models.BooleanField(default=False, verbose_name='est termine')),
                ('event_date', models.DateTimeField(verbose_name="date de l'evenement")),
                ('attendees', models.IntegerField(verbose_name='nombre de participants')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='cree a')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='mis a jour a')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contracts.contracts', verbose_name='contrat')),
                ('support_contact', models.ForeignKey(error_messages={'limit_choices_to': 'This user is not part of the support team.'}, limit_choices_to={'role': 'support'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='contact support')),
            ],
            options={
                'verbose_name': 'evenement',
                'verbose_name_plural': 'evenements',
            },
        ),
    ]