from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'description', 'location']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['date']

    def get_queryset(self):
        queryset = super().get_queryset()
        registered = self.request.query_params.get('registered')
        if registered == 'true':
            user = self.request.user
            registered_events = EventRegistration.objects.filter(user=user).values_list('event_id', flat=True)
            queryset = queryset.filter(id__in=registered_events)
        return queryset


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
