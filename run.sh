#/bin/bash
gunicorn -D -b 0.0.0.0:8000 ACSS.wsgi
