#!/bin/sh
export DJANGO_SETTINGS_MODULE=core.settings
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    echo "DB started"
    done

fi
python manage.py collectstatic --noinput
python manage.py migrate
echo "ВСЕ ОК"
exec "$@"