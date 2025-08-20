from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer, EventRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
