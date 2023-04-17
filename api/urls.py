from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, ClientViewSet, ProspectViewSet, ContractViewSet, EventViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('clients', ClientViewSet, basename='client')
router.register('prospects', ProspectViewSet, basename='prospect')
router.register('contracts', ContractViewSet, basename='contract')
router.register('events', EventViewSet, basename='event')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]