#!/bin/sh

until cd /app3/service3
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A service_3 worker --loglevel=info
