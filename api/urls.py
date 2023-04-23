from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, ClientViewSet, LeadViewSet, ContractViewSet, EventViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('clients', ClientViewSet, basename='client')
router.register('leads', LeadViewSet, basename='lead')
router.register('contracts', ContractViewSet, basename='contract')
router.register('events', EventViewSet, basename='event')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]