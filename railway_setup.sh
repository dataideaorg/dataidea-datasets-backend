#!/bin/bash

# Apply database migrations
python manage.py migrate

# Create superuser from environment variables
python manage.py create_superuser

# Collect static files
python manage.py collectstatic --noinput

# Start gunicorn server
exec gunicorn main.wsgi:application --bind 0.0.0.0:8080 