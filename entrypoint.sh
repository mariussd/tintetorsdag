#!/bin/bash

set -e

nginx -c /usr/share/nginx/nginx.conf

python manage.py migrate
python manage.py runserver
