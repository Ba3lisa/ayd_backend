#!/bin/sh

echo Running startup script: $STARTUP_SH
echo Moving to $WORKING_DIR
cd $WORKING_DIR

echo Running django on port $DJANGO_PORT
python manage.py makemigrations app
python manage.py migrate app
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:$DJANGO_PORT

# DEBUG
tail -f /dev/null
