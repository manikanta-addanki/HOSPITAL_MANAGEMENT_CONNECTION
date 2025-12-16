python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn HOSPITAL_PROJECT.wsgi:application --bind 0.0.0.0:$PORT 

