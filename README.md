# Event Manager API

Event Manager is a REST API service for managing events and user registrations.  
The project is built with **Django REST Framework**, uses **JWT authentication**, and runs via **Docker**.

---

## 📦 Features
- User registration  
- Authentication via JWT (`access` and `refresh` tokens)  
- CRUD operations for events (create, read, update, delete)  
- Event registration for users  
- Filtering events by user registration  
- Interactive API documentation with **Swagger UI**

---

## 🚀 Installation & Run

### 1. Clone the repository

git clone https://github.com/d-komissarchik/event-manager-api.git
cd event-manager-api

### 2. Run the project with Docker

docker-compose up --build

This will:

    Build the Docker image
    Start the PostgreSQL database container
    Run migrations
    Run tests
    Start the development server at http://localhost:8000

### 3. Open the API documentation

http://localhost:8000/swagger/

---

##  Authentication

- Register user: POST /api/auth/register/
Request body:
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "testpassword123"
    }

- Obtain tokens: POST /api/auth/token/
Request body:
    {
      "username": "testuser",
      "password": "testpassword123"
    }

- Refresh access token: POST /api/auth/token/refresh/
Request body:
    {
      "refresh": "<refresh_token>"
    }

---

##  Events

- List events: GET /api/events/

- Filter only registered events: GET /api/events/?registered=true

- Create event: POST /api/events/ (requires authentication)

- Retrieve event: GET /api/events/{id}/

- Update event: PUT /api/events/{id}/

- Delete event: DELETE /api/events/{id}/

---

##  EventsRegistrations

Register for event: POST /api/registrations/
Request body:
    {
      "event": 1
    }

List registrations: GET /api/registrations/

---

##  🧪 Running Tests

Tests are automatically executed when the project is started with Docker Compose.
You can also run them manually:

docker-compose run web python manage.py test

---

## 📂 Project Structure
Event_manager/
├── events/          # Events app (models, views, serializers, tests)
├── users/           # Users app (registration, authentication)
├── Event_manager/   # Main project config
├── requirements.txt
├── Dockerfile
├── docker-compose.yml

---

## ✅ Requirements

Django>=5.0,<6.0
djangorestframework
drf-yasg
djangorestframework-simplejwt
django-filter
gunicorn
psycopg2-binary
drf-yasg


