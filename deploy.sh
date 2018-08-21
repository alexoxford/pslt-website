#!/bin/bash

git pull "https://github.com/alexoxford/pslt-website.git" release
workon django2
python manage.py collectstatic
touch /var/www/www_mydomain_com_wsgi.py