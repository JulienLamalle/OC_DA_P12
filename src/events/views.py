from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from users.models import User
from clients.models import Client
from contracts.models import Contracts
from events.models import Event
from events.serializers import EventSerializer
from events.helpers.event_is_passed import event_is_passed

from users.permissions import IsSalesContactOfAContract, IsSupportContact



class EventListCreateView(ListCreateAPIView):
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticated, IsSalesContactOfAContract]
  
  def get_queryset(self):
    if self.request.user.role == User.SUPPORT and self.request.query_params.get('mind') == 'true':
      return Event.objects.filter(support_contact=self.request.user)
    return Event.objects.all()
  
  def perform_create(self, serializer):
    contract = get_object_or_404(Contracts, pk=self.request.data.get('contract'))
    support_contact = get_object_or_404(User, pk=self.request.data.get('support_contact'))
    if support_contact.role != User.SUPPORT:
      raise ValidationError("This user is not part of the support team.")
    serializer.save(contract=contract, support_contact=support_contact)
    
class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticated, IsSupportContact]
  
  def perform_update(self, serializer):
    if event_is_passed(self.get_object()):
      raise ValidationError("This event is in the past so you can't edit it.")
    serializer.save()