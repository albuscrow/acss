#!/bin/bash
echo ok
cd /home/ac/sssite/
echo okok
gunicorn --reload -b 0.0.0.0:80 ACSS.wsgi
echo okokok
