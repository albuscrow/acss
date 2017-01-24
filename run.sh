#/bin/bash
cd /home/ac/sssite/
gunicorn --reload -b 0.0.0.0:8000 ACSS.wsgi
