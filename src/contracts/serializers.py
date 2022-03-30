from rest_framework import serializers
from contracts.models import Contracts
from users.serializers import UserSerializer
from clients.serializers import ClientSerializer


class ContractSerializer(serializers.ModelSerializer):
  client = ClientSerializer(read_only=True)
  payment_due_date = serializers.DateTimeField(
    format="%d/%m/%Y", input_formats=["%d/%m/%Y"])
  sales_contact = UserSerializer(read_only=True)

  class Meta:
    model = Contracts
    fields = (
        "id",
        "client",
        "amount",
        "payment_due_date",
        "sales_contact",
        "is_signed",
        "is_paid",
    )
