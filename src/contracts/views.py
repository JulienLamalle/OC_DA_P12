from django.shortcuts import get_object_or_404, render


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from contracts.serializers import ContractSerializer
from contracts.models import Contracts
from clients.models import Client
from users.permissions import IsClientSalesContact, IsClientSalesContactForSpecificContract


class ContractListCreateView(ListCreateAPIView):
  queryset = Contracts.objects.all()
  serializer_class = ContractSerializer
  permission_classes = [IsAuthenticated, IsClientSalesContact]

  def perform_create(self, serializer):
    client = get_object_or_404(Client, pk=self.request.data.get('client'))
    serializer.save(client=client, sales_contact=self.request.user)

class ContractRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  queryset = Contracts.objects.all()
  serializer_class = ContractSerializer
  permission_classes = [IsAuthenticated, IsClientSalesContactForSpecificContract]