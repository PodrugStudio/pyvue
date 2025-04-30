# Vue + Flask Docker Application

This is a full-stack application using Vue 3 with Vite for the frontend and Flask for the backend, containerized with Docker.

## Project Structure

```
.
├── backend/           # Flask backend
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/          # Vue 3 frontend
│   ├── src/
│   ├── package.json
│   └── Dockerfile
└── docker-compose.yml # Docker Compose configuration
```

## Prerequisites

- Docker
- Docker Compose
- OrbStack (for running Docker containers)

## Getting Started

1. Clone this repository
2. Run the application using Docker Compose:

```bash
docker-compose up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

## Development

The application is set up with hot-reloading for both frontend and backend:
- Frontend changes will automatically reload in the browser
- Backend changes will automatically restart the Flask server

## API Endpoints

- `GET /api/hello` - Returns a greeting message from the backend 
