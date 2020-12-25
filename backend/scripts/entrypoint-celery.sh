#!/bin/sh

set -e

cd backend
celery -A config worker -l info