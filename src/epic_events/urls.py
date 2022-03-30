"""epic_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from events.views import EventListCreateView, EventRetrieveUpdateDestroyView
from users.views import UserListView, UserDetailView
from clients.views import ClientListCreateView, ClientRetrieveUpdateDestroyView
from contracts.views import ContractListCreateView, ContractRetrieveUpdateDestroyView

urlpatterns = [
    path('management/', admin.site.urls),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('clients/', ClientListCreateView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client'),
    path('contracts/', ContractListCreateView.as_view(), name='contracts'),
    path('contracts/<int:pk>/', ContractRetrieveUpdateDestroyView.as_view(), name='contract'),
    path('events/', EventListCreateView.as_view(), name='events'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event'),
]
