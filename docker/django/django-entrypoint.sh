#!/bin/bash

# You need to make migrations manually:
# python3 manage.py makemigrations fwbm 

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000

exec "$@"