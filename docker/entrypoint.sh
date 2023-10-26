#!/bin/sh

sleep 50
cd service3
source ../venv/bin/activate
sleep 50
python manage.py migrate

exec "$@"