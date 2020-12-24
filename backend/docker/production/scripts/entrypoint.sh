#!/bin/sh

set -e

echo "Waiting for postgres..."

while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.1
done

echo "PostgreSQL started"

cd backend
python manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 config.wsgi:application