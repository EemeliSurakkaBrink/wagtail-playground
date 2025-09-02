run with:
uv run python manage.py runserver

# Run migrations and create superuser
uv run python manage.py migrate
uv run python manage.py createsuperuser

# make migrations
python manage.py makemigrations blog
python manage.py migrate