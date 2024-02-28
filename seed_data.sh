#!/bin/bash
pipenv run python manage.py seed_users --number 10
pipenv run python manage.py seed_amenities --number -1
pipenv run python manage.py seed_facilities --number -1
pipenv run python manage.py seed_rules --number -1
pipenv run python manage.py seed_rooms --number 10
pipenv run python manage.py seed_lists --number 5
pipenv run python manage.py seed_lists --number 5
pipenv run python manage.py seed_reviews --number 15
pipenv run python manage.py seed_reservations --number 5