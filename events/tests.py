from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from events.models import Event, EventRegistration


class EventTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="organizer", password="password123")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_event(self):
        url = "/api/events/"
        data = {
            "title": "Test Event",
            "description": "Some description",
            "location": "Kyiv",
            "organizer": self.user.id,
            "date": (timezone.now() + timedelta(days=1)).isoformat()
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Event.objects.filter(title="Test Event").exists())

    def test_list_events(self):
        Event.objects.create(
            title="Event 1",
            description="Desc",
            location="Lviv",
            organizer=self.user,
            date=timezone.now() + timedelta(days=2)
        )
        url = "/api/events/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_register_for_event(self):
        event = Event.objects.create(
            title="Event 2",
            description="Desc",
            location="Odesa",
            organizer=self.user,
            date=timezone.now() + timedelta(days=3)
        )
        url = "/api/registrations/"
        data = {"event": event.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(EventRegistration.objects.filter(event=event, user=self.user).exists())

    def test_register_for_event_twice(self):
        event = Event.objects.create(
            title="Event 3",
            description="Desc",
            location="Kharkiv",
            organizer=self.user,
            date=timezone.now() + timedelta(days=4)
        )
        EventRegistration.objects.create(event=event, user=self.user)

        url = "/api/registrations/"
        data = {"event": event.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_registered_events_only(self):
        event1 = Event.objects.create(
            title="Event 4",
            description="Desc",
            location="Dnipro",
            organizer=self.user,
            date=timezone.now() + timedelta(days=5)
        )
        event2 = Event.objects.create(
            title="Event 5",
            description="Desc",
            location="Kyiv",
            organizer=self.user,
            date=timezone.now() + timedelta(days=6)
        )
        EventRegistration.objects.create(event=event1, user=self.user)

        url = "/api/events/?registered=true"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        titles = [e["title"] for e in response.data]
        self.assertIn("Event 4", titles)
        self.assertNotIn("Event 5", titles)
