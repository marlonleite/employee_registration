!/bin/bash

python manage.py collectstatic --noinput
python manage.py flush --no-input
python manage.py migrate

# Start server
gunicorn --bind 0.0.0.0:8000 employee_registration.wsgi