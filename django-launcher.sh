#!/bin/bash


# Collect static files command
python3 manage.py collectstatic --noinput

# Apply migrations command
python3 manage.py migrate

# Start server command
python3 manage.py runserver 0.0.0.0:8000