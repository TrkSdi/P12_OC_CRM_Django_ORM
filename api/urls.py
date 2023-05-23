from rest_framework import routers
from django.urls import path, include
from .views import (UserViewSet, ClientViewSet,
                    LeadViewSet, ContractViewSet,
                    EventViewSet, EventStatusViewSet)


router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('clients', ClientViewSet, basename='client')
router.register('leads', LeadViewSet, basename='lead')
router.register('contracts', ContractViewSet, basename='contract')
router.register('events', EventViewSet, basename='event')
router.register('eventstatus', EventStatusViewSet, basename='event_status')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
