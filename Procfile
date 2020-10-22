web: gunicorn InstaClone.wsgiapplication --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate