from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from clients.serializers import ClientSerializer
from clients.models import Client
from users.permissions import IsSales, IsSalesContactOrManager


class ClientListCreateView(ListCreateAPIView):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  permission_classes = [IsAuthenticated, IsSales]
  
  def perform_create(self, serializer):
    if self.request.user.role == 'sales':
      serializer.save(sales_contact=self.request.user)
    serializer.save()
  
class ClientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  permission_classes = [IsAuthenticated, IsSalesContactOrManager]
