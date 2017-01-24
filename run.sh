#!/bin/bash
cd /home/ac/sssite/
gunicorn --reload -b 0.0.0.0:80 ACSS.wsgi
