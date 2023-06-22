#!/bin/bash
#you might need to modify the settings.py to allow certains ip

python3 src/manage.py migrate
python3 src/manage.py runserver #you can specify the ip you want (ie: python3 src/manage.py runserver 10.0.2.15:8000)