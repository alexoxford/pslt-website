#!/bin/bash

git pull origin release
python manage.py collectstatic
touch /var/www/www_mydomain_com_wsgi.py