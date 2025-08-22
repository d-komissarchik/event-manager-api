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

    def create(self, validated_data):
        user = self.context['request'].user
        event = validated_data['event']
        if EventRegistration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("Вже зареєстровано на це подію")
        validated_data['user'] = user
        return super().create(validated_data)
