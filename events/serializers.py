from rest_framework import serializers
from .models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['id', 'user', 'event', 'date']
        read_only_fields = ['user', 'date']

    def create(self, data):
        user = self.context['request'].user
        event = data['event']
        if EventRegistration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("Вже зареєстровано на це подію")
        data['user'] = user
        return super().create(data)
