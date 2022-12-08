web: gunicorn album_review.wsgi:application

release: django-admin migrate --no-input && django-admin collectstatic --no-input