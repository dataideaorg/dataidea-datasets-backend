#!/bin/bash

# Set environment variables for testing
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=securepassword

# Run the management command
python manage.py create_superuser

echo "Test completed. Check above for output." 