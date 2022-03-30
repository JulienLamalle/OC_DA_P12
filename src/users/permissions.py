from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission

from clients.models import Client
from contracts.models import Contracts


class IsSales(BasePermission):
  def has_permission(self, request, view):
    return True if request.method == 'GET' else request.user.role == 'sales'


class IsSalesContactOrManager(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method == 'GET':
      return True
    if request.user.role == 'management':
      return True
    client = get_object_or_404(Client, pk=obj.pk)
    return request.user == client.sales_contact


class IsClientSalesContact(BasePermission):
  def has_permission(self, request, view):
    if request.method == 'GET':
      return True
    client = get_object_or_404(Client, pk=request.data.get('client'))
    return request.user == client.sales_contact


class IsClientSalesContactForSpecificContract(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method == 'GET':
      return True
    if request.user.role == 'management':
      return True
    return request.user == obj.client.sales_contact


class IsSalesContactOfAContract(BasePermission):
  def has_permission(self, request, view):
    if request.method == 'GET':
      return True
    contract = get_object_or_404(Contracts, pk=request.data.get('contract'))
    return request.user == contract.sales_contact


class IsSupportContact(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method == 'GET':
      return True
    if request.user.role == 'management':
      return True
    return request.user == obj.support_contact
