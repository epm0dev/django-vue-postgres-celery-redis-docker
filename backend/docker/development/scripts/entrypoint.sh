#!/bin/sh

set -e

python backend/manage.py collectstatic --noinput
python backend/manage.py runserver 0.0.0.0:8000