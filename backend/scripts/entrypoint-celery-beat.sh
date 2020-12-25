#!/bin/sh

set -e

cd backend
celery -A config beat -l info -s /vol/web/celerbybeat-schedule.db